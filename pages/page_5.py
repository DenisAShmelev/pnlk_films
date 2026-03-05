import streamlit as st

# Настройка страницы (опционально, для лучшей видимости)
st.set_page_config(layout="wide")

st.title("Qwen3.5-397B-A17B")
st.write("Заполните поля ниже:")

# Создаем 5 колонок в один ряд
# st.columns возвращает список контейнеров (col1, col2, ...)
cols = st.columns(5)

# Размещаем поля ввода в каждой колонке
with cols[0]:
    amount = st.number_input("Сумма", min_value=0.0, step=1000.0)

with cols[1]:
    percent = st.number_input("Процент", min_value=0.0, max_value=100.0, step=0.1)

with cols[2]:
    months = st.number_input("Срок в месяцах", min_value=1, step=1)

with cols[3]:
    # Это поле можно сделать доступным только для чтения (disabled), 
    # если прибыль рассчитывается автоматически, или оставить editable.
    profit = st.number_input("Прибыль", min_value=0.0, step=100.0)

with cols[4]:
    total_amount = st.number_input("Сумма с прибылью", min_value=0.0, step=1000.0)

# Пример простой логики (опционально): 
# Если вы хотите, чтобы поля считались автоматически при вводе первых трех значений:
if amount > 0 and percent > 0 and months > 0:
    # Формула: Сумма * (Процент/100) * (Месяцы/12) - пример сложного процента или простого
    calculated_profit = amount * (percent / 100) * (months / 12)
    calculated_total = amount + calculated_profit
    
    # Обновляем значения в сессии, если они не были изменены вручную (упрощенно)
    # В реальном приложении здесь нужна более сложная логика с st.session_state
    st.info(f"Расчетная прибыль: {calculated_profit:.2f}")
    st.info(f"Расчетная сумма с прибылью: {calculated_total:.2f}")
