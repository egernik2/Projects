import flet_test2 as ft
import time
import psycopg2


def main(page: ft.Page):
    page.title = 'Example App'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 500
    page.window.height = 800
    page.scroll = ft.ScrollMode.ADAPTIVE
    host = ft.TextField(label='IP', width=200)
    user_login = ft.TextField(label='Login', width=200)
    user_password = ft.TextField(label='Password', password=True, width=200)
    rg = ft.RadioGroup(content=ft.Row
        (
            [
                ft.Radio(value='mon_reports', label='mon_reports'),
                ft.Radio(value='cservcfg', label='cservcfg')
            ], 
            alignment=ft.MainAxisAlignment.CENTER
        )
    )
    output_area = ft.TextField(label='Output', multiline=True, value=None, read_only=True)

    def add_output(data):
        output_area.value += f'{data}\n'
        page.update()


    def clear_output():
        output_area.value = None
        page.update()


    def connect(e):
        vibor = rg.value
        clear_output()
        add_output('Connecting...')
        with psycopg2.connect(host=host.value, user=user_login.value, password=user_password.value, dbname=rg.value) as conn:
            cur = conn.cursor()
            try:
                if vibor == 'mon_reports':
                    cur.execute('SELECT * FROM dbo.hardware_items;')
                elif vibor == 'cservcfg':
                    cur.execute('SELECT * FROM uts;')
                else:
                    add_output('Вы должны выбрать базу данных!')
                    return
                ans = cur.fetchall()
                for line in ans:
                    add_output(line)
            except Exception as ex:
                add_output('Error:')
                add_output(ex)
        

    page.add(
        ft.Column(
            [
                ft.Text("DB Connector", size=20, text_align='center', weight="bold"),
                ft.Divider(height=30),
                host,
                user_login,
                user_password,
                ft.Text('Database:'),
                rg,
                ft.ElevatedButton("Connect", icon=ft.icons.PLAY_ARROW, on_click=connect, width=200, tooltip='Connect'),
                output_area
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=15,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )


if __name__ == '__main__':
    #ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=80)
    ft.app(target=main)