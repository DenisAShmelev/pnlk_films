import streamlit as st

# --- НАСТРОЙКИ ПО УМОЛЧАНИЮ ---
DEFAULT_AMOUNT = 100000.0
DEFAULT_PERCENT = 12.5
DEFAULT_MONTHS = 12

st.title("Qwen3.5-Plus")

# Инициализация session_state, если значения еще не установлены
if "amount" not in st.session_state:
    st.session_state.amount = DEFAULT_AMOUNT
if "percent" not in st.session_state:
    st.session_state.percent = DEFAULT_PERCENT
if "months" not in st.session_state:
    st.session_state.months = DEFAULT_MONTHS

# Функция пересчета
def calculate():
    amount = st.session_state.amount
    percent = st.session_state.percent
    months = st.session_state.months
    
    if months > 0 and amount > 0:
        # Формула простого процента: Сумма * (Процент/100) * (Месяцы/12)
        profit = amount * (percent / 100) * (months / 12)
        total = amount + profit
    else:
        profit = 0.0
        total = amount
        
    # Сохраняем результаты в session_state
    st.session_state.profit = profit
    st.session_state.total = total

# Заголовок
st.title("Калькулятор доходности")

# Создаем колонки
col1, col2, col3, col4, col5 = st.columns(5)

# --- ВВОДНЫЕ ДАННЫЕ (Триггеры пересчета) ---
# Используем on_change=calculate, чтобы функция запускалась сразу при изменении
with col1:
    st.number_input(
        "Сумма", 
        value=st.session_state.amount, 
        step=1000.0,
        key="amount", 
        on_change=calculate
    )

with col2:
    st.number_input(
        "Процент", 
        value=st.session_state.percent, 
        step=0.1,
        key="percent", 
        on_change=calculate
    )

with col3:
    st.number_input(
        "Срок в месяцах", 
        value=st.session_state.months, 
        step=1,
        key="months", 
        on_change=calculate
    )

# Вызываем пересчет один раз при первой загрузке, чтобы заполнить поля результата
if "profit" not in st.session_state or "total" not in st.session_state:
    calculate()

# --- РЕЗУЛЬТАТЫ (Автоматически обновляемые поля) ---
# Примечание: Чтобы пользователь мог видеть результат сразу, но не ломал логику своими правками,
# мы используем disabled=True. Если нужно разрешить ручную правку с последующим игнорированием авто-расчета,
# логику нужно усложнять (флаг "ручной режим"). Здесь реализован стандартный калькулятор.

with col4:
    st.number_input(
        "Прибыль", 
        value=round(st.session_state.profit, 2), 
        step=0.01,
        key="profit_display",
        disabled=True  # Поле только для чтения, обновляется автоматически
    )

with col5:
    st.number_input(
        "Сумма с прибылью", 
        value=round(st.session_state.total, 2), 
        step=0.01,
        key="total_display",
        disabled=True  # Поле только для чтения, обновляется автоматически
    )

# Дополнительная визуализация (опционально)
st.divider()
st.info(f"💡 Расчет производится автоматически при изменении любых из первых трех параметров.")
