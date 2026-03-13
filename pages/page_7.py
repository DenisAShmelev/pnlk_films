import streamlit as st

# --- НАСТРОЙКИ ПО УМОЛЧАНИЮ ---
DEFAULT_AMOUNT = 100000.0      # Сумма
DEFAULT_PERCENT = 12.5         # Процент годовых
DEFAULT_MONTHS = 12            # Срок в месяцах

# Заголовок страницы
st.title("Qwen2.5-Max")

# Инициализация session_state (для хранения состояния)
if 'amount' not in st.session_state:
    st.session_state.amount = DEFAULT_AMOUNT
if 'percent' not in st.session_state:
    st.session_state.percent = DEFAULT_PERCENT
if 'months' not in st.session_state:
    st.session_state.months = DEFAULT_MONTHS
if 'profit' not in st.session_state:
    st.session_state.profit = 0.0
if 'total_amount' not in st.session_state:
    st.session_state.total_amount = DEFAULT_AMOUNT

# Функция для пересчета значений
def recalculate():
    if st.session_state.months > 0:
        # Формула: Сумма * (Процент / 100) * (Месяцы / 12)
        st.session_state.profit = (
            st.session_state.amount * (st.session_state.percent / 100) * (st.session_state.months / 12)
        )
        st.session_state.total_amount = st.session_state.amount + st.session_state.profit
    else:
        st.session_state.profit = 0.0
        st.session_state.total_amount = st.session_state.amount

# Создаем колонки для размещения элементов в один ряд
col1, col2, col3, col4, col5 = st.columns(5)

# 1. Поле ввода "Сумма"
with col1:
    amount = st.number_input(
        "Сумма", 
        value=st.session_state.amount, 
        step=1000.0,
        key="input_amount",
        on_change=recalculate
    )
    st.session_state.amount = amount  # Обновляем состояние

# 2. Поле ввода "Процент"
with col2:
    percent = st.number_input(
        "Процент", 
        value=st.session_state.percent, 
        step=0.1,
        key="input_percent",
        on_change=recalculate
    )
    st.session_state.percent = percent  # Обновляем состояние

# 3. Поле ввода "Срок в месяцах"
with col3:
    months = st.number_input(
        "Срок в месяцах", 
        value=st.session_state.months, 
        step=1,
        key="input_months",
        on_change=recalculate
    )
    st.session_state.months = months  # Обновляем состояние

# 4. Поле вывода "Прибыль"
with col4:
    profit = st.number_input(
        "Прибыль", 
        value=st.session_state.profit, 
        step=0.01,
        key="input_profit",
        disabled=True  # Делаем поле только для чтения
    )

# 5. Поле вывода "Сумма с прибылью"
with col5:
    total_amount = st.number_input(
        "Сумма с прибылью", 
        value=st.session_state.total_amount, 
        step=0.01,
        key="input_total",
        disabled=True  # Делаем поле только для чтения
    )

# Отображение текущих значений для проверки (можно удалить)
st.write("---")
st.write(f"Текущие вводные: Сумма={st.session_state.amount}, Процент={st.session_state.percent}%, Срок={st.session_state.months} мес.")
