import flet_test2 as ft
import paramiko
import subprocess
import os
import shutil
import time

class T15RawSenderApp(ft.UserControl):
    def build(self):
        # Инициализация полей ввода с фиксированной шириной для лучшей компоновки
        self.label_style = ft.TextStyle(color="white")
        self.host_input = ft.TextField(label="HOST", value="192.168.0.26", width=400, label_style=self.label_style)
        self.login_input = ft.TextField(label="LOGIN", value="user", width=400, label_style=self.label_style)
        self.password_input = ft.TextField(label="PASSWORD", password=True, value="passw0rd", width=400, label_style=self.label_style)
        self.raw_name_input = ft.TextField(label="RAW_NAME", value="t15_raw.tar.gz", width=400, label_style=self.label_style)
        self.builded_name_input = ft.TextField(label="BUILDED_NAME", value="t15_builded.tar.gz", width=400, label_style=self.label_style)
        self.raw_path_input = ft.TextField(label="RAW_PATH", value="/mnt/h/Work/T4300/t15_raw", width=400, label_style=self.label_style)
        self.builded_path_input = ft.TextField(label="BUILDED_PATH", value="/mnt/h/Work/T4300/t15_builded", width=400, label_style=self.label_style)
        self.remote_home_dir_input = ft.TextField(label="REMOTE_HOME_DIR", value="/home/user", width=400, label_style=self.label_style)
        self.output_text = ft.TextField(
            label="Output",
            multiline=True,
            read_only=True,
            expand=True,
            bgcolor="#263238",
            color="white",
            height=300,
            width=500,
            label_style=self.label_style
        )

        # Создание основного контейнера с вертикальной компоновкой
        main_container = ft.Container(
            content=ft.Column(
                [
                    ft.Text("T15 Builder", size=30, weight="bold", color="white", text_align="center"),
                    ft.Divider(height=20, color="white"),
                    self.host_input,
                    self.login_input,
                    self.password_input,
                    self.raw_name_input,
                    self.builded_name_input,
                    self.raw_path_input,
                    self.builded_path_input,
                    self.remote_home_dir_input,
                    ft.Divider(height=20, color="white"),
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                "Start Process",
                                icon=ft.icons.PLAY_ARROW,
                                bgcolor=ft.colors.LIGHT_BLUE,
                                on_click=self.start_process,
                                width=200,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Divider(height=20, color="white"),
                    self.output_text,
                ],
                spacing=15,
                alignment=ft.MainAxisAlignment.START,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            padding=20,
            border_radius=ft.border_radius.all(20),
            bgcolor="#455A64",  # Основной фон контейнера
            shadow=ft.BoxShadow(blur_radius=15, spread_radius=5, color=ft.colors.BLACK26),
        )

        # Возвращаем основной контейнер, центрированный на странице
        return ft.Container(
            content=ft.Row(
                [main_container],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            bgcolor="#37474F",  # Фон страницы
            expand=True,
        )

    def start_process(self, e):
        # Считывание данных с полей ввода
        host = self.host_input.value
        login = self.login_input.value
        password = self.password_input.value
        raw_name = self.raw_name_input.value
        builded_name = self.builded_name_input.value
        raw_path = self.raw_path_input.value
        builded_path = self.builded_path_input.value
        remote_home_dir = self.remote_home_dir_input.value

        # Выполнение процесса и обновление вывода
        try:
            sender = T15RawSender(
                host, login, password, raw_name, builded_name, raw_path, builded_path, remote_home_dir
            )
            sender.get_connection()
            self.append_output("Подключение к хосту установлено.")
            sender.check_old()
            self.append_output("Проверка и удаление старых сырых архивов завершена.")
            sender.compress_data()
            self.append_output("Новый архив создан")
            sender.send_data()
            self.append_output("Архив отправлен")
            self.append_output('Начинаю сборку')
            sender.remote_execute_command(f'sudo {remote_home_dir}/build.sh')
            self.append_output("Сборка завершена. Получаю сборку")
            sender.get_data()
            self.append_output("Сборка получена")
            sender.close_connection()
            self.append_output("Подключение закрыто.")
            self.append_output("Процесс завершён успешно!")
        except Exception as ex:
            self.append_output(f"Ошибка: {ex}")

    def append_output(self, text):
        self.output_text.value += text + "\n"
        self.output_text.update()

class T15RawSender:
    def __init__(self, host, login, password, raw_name, builded_name, raw_path, builded_path, remote_home_dir):
        self.host = host
        self.login = login
        self.password = password
        self.raw_name = raw_name
        self.builded_name = builded_name
        self.raw_path = raw_path
        self.builded_path = builded_path
        self.remote_home_dir = remote_home_dir
        self.raw_full_path = os.path.join(self.raw_path, self.raw_name)
        self.remote_builded_path = os.path.join(self.remote_home_dir, self.builded_name)
        self.builded_full_path = os.path.join(self.builded_path, self.builded_name)

    def get_connection(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.host, username=self.login, password=self.password, timeout=10)

    def _execute_command(self, com, cwd=None):
        res = subprocess.run(com, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=cwd)
        ecode = res.returncode
        if ecode != 0:
            err = res.stderr.decode()
            raise RuntimeError(f"Ошибка при выполнении команды [{com}]: {err}")

    def remote_execute_command(self, com):
        stdin, stdout, stderr = self.ssh.exec_command(com)
        for line in stdout:
            print(line.strip())
            time.sleep(0.1)
        ecode = stdout.channel.recv_exit_status()
        if ecode:
            error_msg = stderr.read().decode()
            raise RuntimeError(f"Ошибка при выполнении удалённой команды [{com}]: {error_msg}")

    def check_old(self):
        if os.path.exists(self.raw_full_path):
            os.remove(self.raw_full_path)

    def compress_data(self):
        self._execute_command(f"tar czf {self.raw_name} t15/*", cwd=self.raw_path)

    def send_data(self):
        self.sftp = self.ssh.open_sftp()
        self.sftp.put(self.raw_full_path, os.path.join(self.remote_home_dir, self.raw_name))
        self.sftp.close()

    def get_data(self):
        if os.path.exists(self.builded_path):
            shutil.rmtree(self.builded_path)
        os.mkdir(self.builded_path)
        self.sftp = self.ssh.open_sftp()
        self.sftp.get(self.remote_builded_path, self.builded_full_path)
        self.sftp.close()

    def close_connection(self):
        self.ssh.close()

def main(page: ft.Page):
    page.title = "T15 Builder"
    page.window_width = 700
    page.window_height = 1100
    page.bgcolor = "#37474F"
    app = T15RawSenderApp()
    page.add(app)

if __name__ == "__main__":
    ft.app(target=main)
