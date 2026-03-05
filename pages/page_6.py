import streamlit as st

# Настройка страницы (опционально, для лучшего отображения)
st.set_page_config(page_title="Калькулятор", layout="wide")

st.title("Qwen3.5-Plus")

# Создаем 5 колонок в один ряд
# ratio=[1, 1, 1, 1, 1] делает колонки одинаковой ширины
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    summa = st.number_input("Сумма", min_value=0.0, step=1000.0)

with col2:
    percent = st.number_input("Процент", min_value=0.0, max_value=100.0, step=0.1)

with col3:
    months = st.number_input("Срок в месяцах", min_value=1, step=1)

with col4:
    # Это поле можно сделать доступным только для чтения (disabled), 
    # если прибыль рассчитывается автоматически, или оставить editable.
    profit = st.number_input("Прибыль", min_value=0.0, step=100.0)

with col5:
    total = st.number_input("Сумма с прибылью", min_value=0.0, step=1000.0)

# Пример отображения введенных данных (для проверки)
if st.button("Показать данные"):
    st.write(f"**Сумма:** {summa}")
    st.write(f"**Процент:** {percent}%")
    st.write(f"**Срок:** {months} мес.")
    st.write(f"**Прибыль:** {profit}")
    st.write(f"**Итого:** {total}")
