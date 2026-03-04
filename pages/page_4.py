import streamlit as st

# Заголовок страницы
st.title("Калькулятор инвестиций")

# Создаем колонки для размещения элементов в один ряд
col1, col2, col3, col4, col5 = st.columns(5)

# В каждой колонке добавляем поле ввода с соответствующей подписью
with col1:
    amount = st.number_input("Сумма", value=1000.0, step=0.01, key="amount")

with col2:
    interest_rate = st.number_input("Процент", value=12.0, step=0.01, key="interest_rate")

with col3:
    term_months = st.number_input("Срок в месяцах", value=2, step=1, key="term_months")

with col4:
    # Поле "Прибыль" защищено от ручного ввода
    profit = st.text_input("Прибыль", value=str(st.session_state.get("profit", 0.0)), disabled=True)

with col5:
    # Поле "Сумма" защищено от ручного ввода
    total_amount = st.text_input("Сумма", value=str(st.session_state.get("total_amount", 0.0)), disabled=True)

# Функция для расчета
def calculate_profit(amount, interest_rate, term_months):
    if amount > 0 and interest_rate > 0 and term_months > 0:
        return (amount / 100 * interest_rate) / 12 * term_months
    return 0.0

# Выполняем расчет при каждом изменении значений
if "amount" in st.session_state and "interest_rate" in st.session_state and "term_months" in st.session_state:
    amount = st.session_state["amount"]
    interest_rate = st.session_state["interest_rate"]
    term_months = st.session_state["term_months"]

    # Расчет по формуле
    calculated_profit = calculate_profit(amount, interest_rate, term_months)
    
    # Обновляем состояние сессии для полей "Прибыль" и "Сумма"
    st.session_state.profit = calculated_profit
    st.session_state.total_amount = amount + calculated_profit

# Обновляем значения в полях "Прибыль" и "Сумма"
profit = st.session_state.get("profit", 0.0)
total_amount = st.session_state.get("total_amount", 0.0)

# Обновляем текстовые поля в интерфейсе
with col4:
    st.text_input("Прибыль", value=f"{profit:.2f}", disabled=True)

with col5:
    st.text_input("Сумма", value=f"{total_amount:.2f}", disabled=True)
