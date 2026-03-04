import streamlit as st

# Заголовок страницы
st.title("Калькулятор инвестиций")

# Создаем колонки для размещения элементов в один ряд
col1, col2, col3, col4, col5 = st.columns(5)

# В каждой колонке добавляем поле ввода с соответствующей подписью
with col1:
    amount = st.number_input("Сумма", value=1000.0, step=0.01)

with col2:
    interest_rate = st.number_input("Процент", value=12.0, step=0.01)

with col3:
    term_months = st.number_input("Срок в месяцах", value=2, step=1)

with col4:
    # Поле "Прибыль" будет обновляться после расчета
    profit = st.number_input("Прибыль", value=0.0, step=0.01)

with col5:
    total_amount = st.number_input("Сумма", value=0.0, step=0.01)

# Кнопка для расчета
if st.button("Рассчитать"):
    # Проверяем, что введенные значения корректны
    if amount > 0 and interest_rate > 0 and term_months > 0:
        # Расчет по формуле
        a = (amount / 100 * interest_rate) / 12 * term_months
        
        # Выводим результат текстом
        st.success(f"Расчетная прибыль: {a:.2f}")
        
        # Обновляем поле ввода "Прибыль"
        profit = a
        st.session_state.profit = a  # Сохраняем значение в состоянии сессии
    else:
        st.error("Пожалуйста, убедитесь, что все поля заполнены корректно.")

# Обновляем поле ввода "Прибыль" из состояния сессии
if 'profit' in st.session_state:
    profit = st.number_input("Прибыль", value=st.session_state.profit, step=0.01)
