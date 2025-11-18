import customtkinter as ctk
from PIL import Image, ImageTk
import tkinter as tk

# Настройка темы
ctk.set_appearance_mode("System")  # Тема: System (по умолчанию), Light или Dark
ctk.set_default_color_theme("blue")  # Тема цветов: blue, green, dark-blue

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Основные параметры окна
        self.title("Красная и Синяя команды")
        self.geometry("1000x800")  # Увеличиваем размер окна

        # Разделение на две колонки
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Красная команда
        self.red_frame = ctk.CTkFrame(self)
        self.red_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.create_team_section(self.red_frame, "Красная команда", "red", "image")

        # Синяя команда
        self.blue_frame = ctk.CTkFrame(self)
        self.blue_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.create_team_section(self.blue_frame, "Синяя команда", "blue", "blue_image")

    def create_team_section(self, parent, team_name, color, image_prefix):
        # Заголовок команды
        team_label = ctk.CTkLabel(
            parent,
            text=team_name,
            font=("Arial", 16, "bold"),
            text_color=color
        )
        team_label.pack(pady=(10, 20))

        # Создаем 10 блоков заданий
        for i in range(1, 11):  # Теперь 10 блоков вместо 3
            task_frame = ctk.CTkFrame(parent)
            task_frame.pack(pady=10, fill="both", expand=True)

            # Номер задания
            task_number_label = ctk.CTkLabel(
                task_frame,
                text=f"Задание {i}",
                font=("Arial", 12, "bold")
            )
            task_number_label.pack(side="left", padx=10)

            # Поле для ответа
            answer_entry = ctk.CTkEntry(task_frame, placeholder_text="Введите ответ")
            answer_entry.pack(side="left", padx=10)

            # Кнопка проверки ответа
            check_button = ctk.CTkButton(
                task_frame,
                text="Проверить",
                command=lambda entry=answer_entry: self.check_answer(entry)
            )
            check_button.pack(side="left", padx=10)

            # Результат ответа
            result_label = ctk.CTkLabel(task_frame, text="")
            result_label.pack(side="left", padx=10)

            # Окно с картинкой под полем ввода
            image_label = self.create_clickable_image_label(task_frame, f"{image_prefix}{i}.jpg")
            image_label.pack(side="left", padx=10, pady=(10, 0))  # Добавляем отступ сверху

    def create_clickable_image_label(self, parent, image_path):
        try:
            # Открываем изображение
            image = Image.open(image_path)
            # Уменьшаем размер изображения для отображения в основном окне
            thumbnail = image.resize((150, 150), Image.LANCZOS)  # Размер миниатюры
            thumbnail_photo = ImageTk.PhotoImage(thumbnail)

            # Создаем Label для миниатюры
            thumbnail_label = ctk.CTkLabel(parent, image=thumbnail_photo, text="")
            thumbnail_label.image = thumbnail_photo  # Сохраняем ссылку на изображение

            # Добавляем обработчик клика
            thumbnail_label.bind("<Button-1>", lambda event, img=image: self.open_fullscreen_image(img))

            return thumbnail_label
        except FileNotFoundError:
            error_label = ctk.CTkLabel(parent, text=f"Изображение {image_path} не найдено.")
            return error_label

    def open_fullscreen_image(self, image):
        # Создаем новое окно для отображения изображения на весь экран
        fullscreen_window = ctk.CTkToplevel(self)
        fullscreen_window.title("Изображение на весь экран")
        fullscreen_window.geometry(f"{image.width}x{image.height}")  # Размер окна соответствует размеру изображения

        # Отображаем изображение в новом окне
        photo = ImageTk.PhotoImage(image)
        image_label = ctk.CTkLabel(fullscreen_window, image=photo, text="")
        image_label.image = photo  # Сохраняем ссылку на изображение
        image_label.pack(fill="both", expand=True)

    def check_answer(self, entry):
        # Пример проверки ответа (можно заменить на реальную логику)
        answer = entry.get()
        if answer.lower() == "верный ответ":
            result_label = ctk.CTkLabel(entry.master, text="Правильно!", text_color="green")
        else:
            result_label = ctk.CTkLabel(entry.master, text="Неверно!", text_color="red")
        result_label.pack(side="left", padx=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()