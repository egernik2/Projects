import paramiko
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.console import Console
import os

console = Console()

def download_file_via_ssh(hostname: str, username: str, password: str, remote_path: str, local_path: str):
    # Подключение к удалённой машине по SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}"), transient=True) as progress:
        task = progress.add_task(f"[cyan]Подключение к {hostname}...", total=None)  # Задача без общего прогресса
        # Имитация процесса подключения
        ssh.connect(hostname, username=username, password=password, timeout=10)

    # Получаем размер файла на удалённой машине
    stdin, stdout, stderr = ssh.exec_command(f"stat -c%s {remote_path}")
    file_size = int(stdout.read().strip())

    # Создаем прогресс-бар
    with Progress() as progress:
        task = progress.add_task(f"[cyan]Загрузка {os.path.basename(remote_path)}...", total=file_size)

        # Открываем SFTP-сессию для скачивания файла
        with ssh.open_sftp() as sftp:
            with sftp.file(remote_path, 'rb') as remote_file:
                with open(local_path, 'wb') as local_file:
                    while True:
                        chunk = remote_file.read(8192)  # Читаем файл по частям
                        if not chunk:
                            break
                        local_file.write(chunk)
                        # Обновляем прогресс
                        progress.update(task, advance=len(chunk))

    console.print(f"[bold green]Файл успешно загружен и сохранен как {local_path}")

# Пример использования
hostname = "10.5.59.30"  # Адрес удалённой машины
username = "user"     # Имя пользователя
password = "passw0rd"     # Пароль
remote_path = "/home/user/rams-kp_2.0.21crpro_16770_3576_3580_astra1.6.tar.gz"  # Путь к файлу на удалённой машине
local_path = remote_path.split("/")[-1]  # Путь для сохранения файла на локальной машине

download_file_via_ssh(hostname, username, password, remote_path, local_path)