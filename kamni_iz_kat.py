import streamlit as st

st.title('Сколько я нафармил')
red = st.number_input(label='Красные камни', min_value=0, max_value=100000, step=1)
green = st.number_input(label='Зелёные камни', min_value=0, max_value=100000, step=1)
blue = st.number_input(label='Синие камни', min_value=0, max_value=100000, step=1)
price = st.number_input(label='Цена', min_value=3.9, max_value=5.0, step=0.1)
aa_cur = st.number_input(label='Древняя адена', min_value=0, max_value=100000000, step=1)
red_con = 10
green_con = 5
blue_con = 3
if st.button(label='Посчитать'):
    if aa_cur:
        aa = (red * red_con) + (green * green_con) + (blue * blue_con) + aa_cur
    else:
        aa = (red * red_con) + (green * green_con) + (blue * blue_con)
    adena = int(aa * price)
    st.text(f'Кол-во древних аден: {aa} шт.')
    st.text(f'Стоимость: {adena} аден')