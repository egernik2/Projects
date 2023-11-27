import dearpygui.dearpygui as dpg

def auth():
    username = dpg.get_value('username')
    password = dpg.get_value('password')
    print (username)
    print (password)

    with dpg.window(label='Check info'):
        dpg.add_text('Login: {}'.format(username))
        dpg.add_text('Password: {}'.format(password))

def start():
    dpg.create_context()
    dpg.create_viewport(title='Application', width=800, height=800)

def main():
    with dpg.window(label='Workstation', width=230, pos=(300, 300)):
        dpg.add_text('Wellcome to Workstation', tag='auth')
        dpg.add_input_text(label='Username', tag='username')
        dpg.add_input_text(label='Password', tag='password', password=True)
        with dpg.group(horizontal=True):
            dpg.add_button(label='Login', callback=auth)
            dpg.add_button(label='Exit', callback=lambda: exit())

def load():
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()

if __name__ == '__main__':
    start()
    main()
    load()