import streamlit as st

# Заголовок страницы
st.title("Калькулятор инвестиций")

# Инициализация состояния сессии
if "profit" not in st.session_state:
    st.session_state.profit = 0.0
if "total_amount" not in st.session_state:
    st.session_state.total_amount = 0.0

# Функция для расчета
def calculate_profit():
    # Получаем значения из session_state
    amount = st.session_state.get("amount", 0.0)
    interest_rate = st.session_state.get("interest_rate", 0.0)
    term_months = st.session_state.get("term_months", 0)

    # Проверяем, что все значения корректны
    if amount > 0 and interest_rate > 0 and term_months > 0:
        # Расчет по формуле
        calculated_profit = (amount / 100 * interest_rate) / 12 * term_months
        st.session_state.profit = calculated_profit
        st.session_state.total_amount = amount + calculated_profit
    else:
        # Если данные некорректны, сбрасываем значения
        st.session_state.profit = 0.0
        st.session_state.total_amount = 0.0

    # Выводим результат текстом
    if st.session_state.profit > 0:
        st.success(f"Расчетная прибыль: {st.session_state.profit:.2f}, Сумма с прибылью: {st.session_state.total_amount:.2f}")
    else:
        st.error("Пожалуйста, убедитесь, что все поля заполнены корректно.")

# Создаем колонки для размещения элементов в один ряд
col1, col2, col3, col4, col5 = st.columns(5)

# Поле ввода "Сумма"
with col1:
    st.number_input(
        "Сумма",
        value=1000.0,
        step=0.01,
        key="amount",
        on_change=calculate_profit
    )

# Поле ввода "Процент"
with col2:
    st.number_input(
        "Процент",
        value=12.5,
        step=0.01,
        key="interest_rate",
        on_change=calculate_profit
    )

# Поле ввода "Срок в месяцах"
with col3:
    st.number_input(
        "Срок в месяцах",
        value=2,
        step=1,
        key="term_months",
        on_change=calculate_profit
    )

# Поле "Прибыль" (только для чтения)
with col4:
    st.text_input(
        "Прибыль",
        value=f"{st.session_state.profit:.2f}",
        disabled=True,
        key="profit_display"
    )

# Поле "Сумма с прибылью" (только для чтения)
with col5:
    st.text_input(
        "Сумма с прибылью",
        value=f"{st.session_state.total_amount:.2f}",
        disabled=True,
        key="total_amount_display"
    )
