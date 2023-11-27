import dearpygui.dearpygui as dpg

l = ['item', 'item']

def callback_func():
    l.append('item by btn')
    dpg.configure_item(listbox, items=l)

dpg.create_context()
dpg.create_viewport(title='My first DearPyGui')

with dpg.window(label='Tutorial'):
    listbox = dpg.add_listbox(items=l, label='Testing')
    dpg.add_button(label='Add more', callback=callback_func)


dpg.show_item_registry()
dpg.show_debug()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()