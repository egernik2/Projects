import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport()
dpg.setup_dearpygui()

def set_listbox_size(sender):
    # Изменяем ширину списка
    dpg.set_item_height(listbox, height=200)

with dpg.handler_registry():
    dpg.create_context()
    with dpg.window(label="Window example"):
        listbox = dpg.add_listbox(items=["Element 1", "Element 2", "Element 3"])
        button = dpg.add_button(label="Change list size")
        dpg.add_button(label="Exit", callback=dpg.stop_dearpygui)
    
    dpg.set_item_callback(button, set_listbox_size)  # Устанавливаем обратный вызов для кнопки

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()