import npyscreen
import time
import threading

class TestApp(npyscreen.NPSApp):
    def main(self):
        self.F  = npyscreen.Form(name = "Welcome to Npyscreen",)
        self.text  = self.F.add(npyscreen.TitleText, name = "Text:",)
        self.btn = self.F.add(npyscreen.ButtonPress, name='Press me', relx=2, rely=4, when_pressed_function=self.thread_for_func)
        self.box = self.F.add(npyscreen.BoxTitle, name="Полученный ответ", editable=True, rely=6)
        self.F.edit()

    def pressed(self):
        l = [i for i in range(50)]
        for i in l:
            self.box.values.append(str(i))
            self.box.update()
            time.sleep(0.5)

    def thread_for_func(self):
        thread = threading.Thread(target=self.pressed, daemon=True)
        thread.start()


if __name__ == "__main__":
    App = TestApp()
    App.run()