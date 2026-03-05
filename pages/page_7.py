import streamlit as st

# Заголовок страницы
st.title("Qwen2.5-Max")

# Создаем колонки для размещения элементов в один ряд
col1, col2, col3, col4, col5 = st.columns(5)

# Поле ввода "Сумма"
with col1:
    amount = st.number_input("Сумма", value=0.0, step=0.01)

# Поле ввода "Процент"
with col2:
    percent = st.number_input("Процент", value=0.0, step=0.01)

# Поле ввода "Срок в месяцах"
with col3:
    months = st.number_input("Срок в месяцах", value=0, step=1)

# Поле ввода "Прибыль"
with col4:
    profit = st.number_input("Прибыль", value=0.0, step=0.01)

# Поле ввода "Сумма с прибылью"
with col5:
    total_amount = st.number_input("Сумма с прибылью", value=0.0, step=0.01)
