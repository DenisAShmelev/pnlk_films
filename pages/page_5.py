import streamlit as st

# --- НАСТРОЙКИ ПО УМОЛЧАНИЮ ---
DEFAULT_AMOUNT = 100000.0
DEFAULT_PERCENT = 12.5
DEFAULT_MONTHS = 12

st.title("Калькулятор доходности")

# Функция для пересчета значений
def calculate_values():
    # Получаем текущие значения из session_state (или дефолтные, если их еще нет)
    amount = st.session_state.get("amount", DEFAULT_AMOUNT)
    percent = st.session_state.get("percent", DEFAULT_PERCENT)
    months = st.session_state.get("months", DEFAULT_MONTHS)
    
    # Логика расчета (простой процент)
    if months > 0 and amount > 0:
        profit = amount * (percent / 100) * (months / 12)
        total = amount + profit
    else:
        profit = 0.0
        total = amount if amount > 0 else 0.0
    
    # Округляем до 2 знаков после запятой для красоты
    st.session_state["profit"] = round(profit, 2)
    st.session_state["total"] = round(total, 2)

# Инициализация состояния при первом запуске
if "amount" not in st.session_state:
    st.session_state.amount = DEFAULT_AMOUNT
if "percent" not in st.session_state:
    st.session_state.percent = DEFAULT_PERCENT
if "months" not in st.session_state:
    st.session_state.months = DEFAULT_MONTHS
if "profit" not in st.session_state:
    st.session_state.profit = 0.0
if "total" not in st.session_state:
    st.session_state.total = 0.0

# Создаем колонки
col1, col2, col3, col4, col5 = st.columns(5)

# 1. Поле "Сумма"
with col1:
    st.number_input(
        "Сумма", 
        key="amount",  # Ключ связывает виджет с переменной состояния
        step=1000.0,
        on_change=calculate_values  # При изменении запускаем пересчет
    )

# 2. Поле "Процент"
with col2:
    st.number_input(
        "Процент", 
        key="percent", 
        step=0.1,
        on_change=calculate_values
    )

# 3. Поле "Срок в месяцах"
with col3:
    st.number_input(
        "Срок в месяцах", 
        key="months", 
        step=1,
        on_change=calculate_values
    )

# 4. Поле "Прибыль" (Только для чтения или редактируемое?)
# Обычно такие поля делают доступными только для чтения, чтобы пользователь не сломал логику.
# Если нужно разрешить ручной ввод, уберите параметр disabled=True, но тогда логика усложнится.
with col4:
    st.number_input(
        "Прибыль", 
        key="profit", 
        step=0.01,
        disabled=True  # Запрещаем ручное редактирование, так как это результат расчета
    )

# 5. Поле "Сумма с прибылью"
with col5:
    st.number_input(
        "Сумма с прибылью", 
        key="total", 
        step=0.01,
        disabled=True
    )

# Первоначальный расчет при загрузке страницы
calculate_values()
