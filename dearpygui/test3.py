import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)


def check_login(sender, data):
    login = dpg.get_value("login")
    password = dpg.get_value("password")
    if login == "admin" and password == "qwerty":
        dpg.show_item("success")
        dpg.add_text(default_value='{}:{}'.format(login, password), parent='Status')
    else:
        dpg.show_item("error")


with dpg.window(label="Window"):
    dpg.add_text("Enter username and password")
    dpg.add_input_text(label="Login", width=200, tag='login')
    dpg.add_input_text(label="Password", width=200, password=True, tag='password')
    dpg.add_button(label="Enter", callback=check_login)
    with dpg.child_window(tag="Status"):
        dpg.add_text("Success!", tag="success", color=[0, 255, 0], parent="Status")
        dpg.add_text("Error", tag="error", color=[255, 0, 0], parent="Status")
        dpg.hide_item("success")
        dpg.hide_item("error")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()