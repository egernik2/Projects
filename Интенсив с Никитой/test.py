import textwrap
import npyscreen
import sqlite3
import webbrowser


class TestApp(npyscreen.NPSApp):
    def main(self):
        npyscreen.setTheme(npyscreen.Themes.BlackOnWhiteTheme)
        F  = npyscreen.Form(name = "Добро пожаловать",)
        self.sel = F.add(npyscreen.SelectOne, values=['https://vk.com', 'https://google.com', 'https://youtube.com'], max_height=4, scroll_exit=True)
        self.bt = F.add(npyscreen.ButtonPress, name="Открыть", when_pressed_function=self.pressed)
        self.pp = F.add(npyscreen.Pager, rely=8, values=['Test message'], scroll_exit=True)
        F.edit()
            

    def pressed(self):
        npyscreen.notify_confirm(f'Вы выбрали {self.sel.get_selected_objects()[0]}', title="Подтверждение", form_color='STANDOUT', wrap=True, wide=False, editw=0)
        self.pp.values = [f'Открыто {self.sel.get_selected_objects()[0]}']
        self.pp.update()
        webbrowser.open(self.sel.get_selected_objects()[0])


if __name__ == "__main__":
    App = TestApp() 
    App.run()