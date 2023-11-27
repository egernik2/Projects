import dearpygui.dearpygui as dpg

dpg.create_context()

def check_passwd(sender, app_data):
    username = dpg.get_value('username')
    password = dpg.get_value('password')
    if username == 'egernik2' and password == 'suro03xulo':
        dpg.delete_item('main_window')
        with dpg.window(modal=True, label='Pure love', tag='love', no_close=True, no_collapse=True):
            dpg.add_text('I love Kulikova Margarita!')
            dpg.add_button(label='Close', callback=lambda: dpg.delete_item('love'))
    else:
        with dpg.window(modal=True, label='Error', tag='incorrect_window', no_collapse=True, on_close=lambda: dpg.delete_item('incorrect_window')):
            dpg.add_text('Username or password is incorrect!')
            dpg.add_button(label='Ok', callback=lambda: dpg.delete_item('incorrect_window'))
            dpg.configure_item('password', default_value='')


with dpg.window(label="Some App", height=100, width=300, tag='main_window', no_close=True, no_collapse=True):
    dpg.add_input_text(label='Username', tag='username')
    dpg.add_input_text(label='Password', password=True, tag='password')
    dpg.add_button(label='Submit', callback=check_passwd)
    #dpg.add_text('Some text...', tag='text_label')

    

dpg.create_viewport(title='Application', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

#(dpg.get_value('username'), dpg.get_value('password'))