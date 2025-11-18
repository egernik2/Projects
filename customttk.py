import customtkinter as ctk
import keyboard

KEYS = ['z', 'x', 'c', 'v', 'b']

# Set appearance mode and default color theme
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def on_key_press(event):
    if event.keysym == 'z':
        print('Отвечает очкастое быдло')
    elif event.keysym == 'x':
        print('Отвечает жирное быдло')
    elif event.keysym == 'c':
        print('Отвечает ебаное быдло')
    elif event.keysym == 'v':
        print('Отвечает ссаное быдло')
    elif event.keysym == 'b':
        print('Отвечает ебучее быдло')

    # app.unbind("<Key>")  # Убираем привязку после нажатия 'a'

# Create the main window
app = ctk.CTk()
app.title("Hello CustomTkinter")
app.geometry("400x200")

# Add a label
label = ctk.CTkLabel(app, text="Hello, CustomTkinter!", font=("Helvetica", 20))
label.pack(pady=20)
app.bind('<Key>', on_key_press)

# Add a button
button = ctk.CTkButton(app, text="Click Me", command=lambda: print("Button clicked!"))
button.pack(pady=10)

# Run the application
app.mainloop()