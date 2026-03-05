import streamlit as st

# --- НАСТРОЙКИ ПО УМОЛЧАНИЮ ---
DEFAULT_AMOUNT = 100000.0      # Сумма
DEFAULT_PERCENT = 12.5         # Процент годовых
DEFAULT_MONTHS = 12            # Срок в месяцах

# Заголовок страницы
st.title("Qwen3.5-397B-A17B")

# Создаем колонки для размещения элементов в один ряд
col1, col2, col3, col4, col5 = st.columns(5)

# 1. Поле ввода "Сумма"
with col1:
    amount = st.number_input(
        "Сумма", 
        value=DEFAULT_AMOUNT, 
        step=1000.0,
        key="input_amount"
    )

# 2. Поле ввода "Процент"
with col2:
    percent = st.number_input(
        "Процент", 
        value=DEFAULT_PERCENT, 
        step=0.1,
        key="input_percent"
    )

# 3. Поле ввода "Срок в месяцах"
with col3:
    months = st.number_input(
        "Срок в месяцах", 
        value=DEFAULT_MONTHS, 
        step=1,
        key="input_months"
    )

# Логика расчета (опционально, чтобы поля справа заполнялись автоматически)
# Формула: Прибыль = Сумма * (Процент / 100) * (Месяцы / 12)
calculated_profit = amount * (percent / 100) * (months / 12)
calculated_total = amount + calculated_profit

# 4. Поле ввода "Прибыль"
with col4:
    profit = st.number_input(
        "Прибыль", 
        value=round(calculated_profit, 2), 
        step=0.01,
        key="input_profit"
    )

# 5. Поле ввода "Сумма с прибылью"
with col5:
    total_amount = st.number_input(
        "Сумма с прибылью", 
        value=round(calculated_total, 2), 
        step=0.01,
        key="input_total"
    )

# Отображение текущих настроек по умолчанию (для наглядности, можно удалить)
with st.expander("Настройки по умолчанию"):
    st.write(f"Стартовая сумма: {DEFAULT_AMOUNT}")
    st.write(f"Стартовый процент: {DEFAULT_PERCENT}%")
    st.write(f"Стартовый срок: {DEFAULT_MONTHS} мес.")
