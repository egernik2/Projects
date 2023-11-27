import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)

def widget_row_edit(sender, app_data, user_data):
    with dpg.window(label='Item Editor', width=500, height=150) as w:
        dpg.configure_item(w, on_close=lambda: dpg.delete_item(w))
        if user_data is None:
            for name in user_data:
                dpg.add_input_text(label=name)
        else:
            for name, value in user_data:
                dpg.add_input_text(label=name, default_value=value)
        with dpg.group(horizontal=True):
            dpg.add_button(label='Submit')
            dpg.add_button(label='Cancel', callback=lambda: dpg.delete_item(w))

FIELDS = ('ID', 'Number', 'Name', 'State')

with dpg.window(label='Tickets Viewer', tag='main_window'):
    with dpg.table(header_row=True, row_background=True, borders_innerV=False, borders_outerV=True, borders_innerH=True, borders_outerH=True) as t:
        for field_name in FIELDS:   
            dpg.add_table_column(label=field_name)
        for i in range(0, 4):
            with dpg.table_row(tag='row_{}'.format(i)) as row:
                for j in range(0, 4):
                    dpg.add_text(f"Row{i} Column{j}")
                    with dpg.popup(dpg.last_item(), mousebutton=dpg.mvMouseButton_Right):
                        dpg.add_text('Row: {}'.format(i+1))
                        dpg.add_separator()
                        dpg.add_button(label='New', callback=widget_row_edit, user_data=[f for f in FIELDS])
                        dpg.add_button(label='Edit', callback=widget_row_edit, user_data=[(f, 'value') for f in FIELDS])
                        dpg.add_button(label='Remove')
            print (dpg.get_item_children(row))

# with dpg.window(label='Item Editor', modal=True, show=True):
#     dpg.add_text('New')
#     with dpg.group(horizontal=True):
#         dpg.add_button(label='Submit')
#         dpg.add_button(label='Cancel')




#dpg.show_item_registry()
#dpg.show_debug()
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("main_window", True)
dpg.start_dearpygui()
dpg.destroy_context()