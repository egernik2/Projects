import flet as ft

def main(page: ft.Page):
    page.title = "Мое первое Flet приложение"
    page.window_width = 800 # type: ignore
    page.window_height = 600 # type: ignore

    # Добавьте здесь свои компоненты
    # Например, текстовое поле
    name_input = ft.TextField(label="Имя")
    text_output = ft.Text(value="Your name is: ")
    
    # Например, кнопка
    submit_button = ft.ElevatedButton("Отправить", on_click=lambda e: print(name_input.value))

    # Добавьте компоненты на страницу
    page.add(name_input)
    page.add(submit_button)

ft.app(target=main)