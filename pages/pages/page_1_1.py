import streamlit as st
import pandas as pd

st.title("Таблица с цветным текстом в первом столбце")

# Данные
df = pd.DataFrame({
    'Имя': ['page_1_1.py', 'Борис', 'Светлана', 'Дмитрий', 'Елена'],
    'Возраст': [25, 30, 28, 35, 22],
    'Город': ['Москва', 'СПб', 'Казань', 'Новосибирск', 'Екатеринбург']
})

# Стилизация
styled_df = df.style.set_properties(
    subset=['Имя'],
    **{
        'color': '#D9D9D9',
        'font-weight': '500'
    }
).set_table_styles([
    {'selector': 'th', 'props': [('background-color', '#f0f0f0')]}
])

# Вывод
st.dataframe(styled_df, use_container_width=True)
