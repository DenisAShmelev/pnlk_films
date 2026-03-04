import streamlit as st

# Заголовок страницы
st.title("Калькулятор инвестиций")

# Создаем колонки для размещения элементов в один ряд
col1, col2, col3, col4, col5 = st.columns(5)

# В каждой колонке добавляем поле ввода с соответствующей подписью
with col1:
    amount = st.number_input("Сумма", value=0.0, step=0.01)

with col2:
    interest_rate = st.number_input("Процент", value=0.0, step=0.01)

with col3:
    term_months = st.number_input("Срок в месяцах", value=0, step=1)

with col4:
    profit = st.number_input("Прибыль", value=0.0, step=0.01)

with col5:
    total_amount = st.number_input("Сумма", value=0.0, step=0.01)

# Можно добавить дополнительную логику или кнопку для расчетов
if st.button("Рассчитать"):
    st.write("Здесь будет результат расчета")
