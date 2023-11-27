import textwrap
import npyscreen
import sqlite3


def wrap_message_lines(message, line_length):
    lines = []
    for line in message.split('\n'):
        lines.extend(textwrap.wrap(line.rstrip(), line_length))
    return lines


class TestApp(npyscreen.NPSApp):
    def main(self):
        # These lines create the form and populate it with widgets.
        # A fairly complex screen in only 8 or so lines of code - a line for each control.
        F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        self.t  = F.add(npyscreen.TitleText, name = "Запрос:", value='select * from problems')
        self.fn2 = F.add(npyscreen.TitleFilenameCombo, name="База данных:")
        self.bt = F.add(npyscreen.ButtonPress, name="Найти", when_pressed_function=self.pressed, rely=4)
        self.my_textbox = F.add(MyBox, name="Полученный ответ", max_height=30, rely=6)
        self.my_textbox.when_cursor_moved = self._changed
        self.ml = F.add(npyscreen.Pager, editable=False)
        self.ml.values = []
        F.edit()

    def _changed(self):
        #dir(self.my_textbox)
        selected_cursor_line = self.my_textbox.entry_widget.cursor_line
        message = str(self.my_textbox.entry_widget.values[selected_cursor_line])
        self.ml.values = wrap_message_lines(message, 160)
        self.ml.update()
        #npyscreen.notify_confirm(message, title="Message", form_color='STANDOUT', wrap=True, wide=False, editw=0)
            

    def pressed(self):
        # выполнение запроса в базу данных
        query = self.t.value
        conn = sqlite3.connect(self.fn2.value)
        c = conn.cursor()
        c.execute(query)
        results = c.fetchall()
        # вывод результатов поиска
        for result in results:
            self.my_textbox.values.append(str(result))
        conn.close()
        # results = [[i, 'test{}'.format(i)] for i in range(10)]
        #self.ml.update()
        self.my_textbox.update()
        self._changed()


class MyBox(npyscreen.BoxTitle):
    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)


if __name__ == "__main__":
    App = TestApp()
    App.run()