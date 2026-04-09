import streamlit as st
import pandas as pd
import requests

# Настройка страницы
st.set_page_config(page_title="Тест", layout="wide")

# Заголовок
st.title("Тест с сохранением результатов")

# Вопросы и варианты ответов
questions = [
    "Какой язык программирования вы предпочитаете?",
    "Какой фреймворк вам больше нравится?",
    "Какой тип данных вы используете чаще всего?"
]

options = ["Ответ 1", "Ответ 2", "Ответ 3", "Ответ 4", "Ответ 5", "Ответ 6"]

# Инициализация состояния для ответов
if "answers" not in st.session_state:
    st.session_state.answers = {q: None for q in questions}

# Функция для отображения вопросов и радио-кнопок
def display_questions():
    for question in questions:
        col1, col2 = st.columns([2, 3])  # Разделение на левую и правую части
        with col1:
            st.write(f"**{question}**")
        with col2:
            selected_option = st.radio(
                label="Выберите один ответ",
                options=options,
                index=options.index(st.session_state.answers[question]) if st.session_state.answers[question] else 0,
                key=question,
                horizontal=True
            )
            st.session_state.answers[question] = selected_option

# Отображение вопросов
display_questions()

# Кнопка для сохранения результатов
if st.button("Сохранить результаты"):
    # Создание таблицы с результатами
    results = []
    for question, answer in st.session_state.answers.items():
        row = [question] + ["✓" if option == answer else "" for option in options]
        results.append(row)

    df_results = pd.DataFrame(results, columns=["Вопрос"] + options)

    # Отображение таблицы
    st.write("\nРезультаты теста:")
    st.dataframe(df_results)

    # Сохранение результатов в файл на GitHub
    try:
        # Преобразование DataFrame в CSV
        csv_data = df_results.to_csv(index=False)

        # Загрузка файла на GitHub через API
        github_token = st.secrets.get("GITHUB_TOKEN")  # Убедитесь, что добавили токен в secrets.toml
        repo_owner = "your_github_username"
        repo_name = "your_repo_name"
        file_path = "results.csv"

        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}"
        headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # Получение SHA текущего файла (если он существует)
        response = requests.get(url, headers=headers)
        sha = response.json().get("sha") if response.status_code == 200 else None

        # Обновление или создание файла
        data = {
            "message": "Обновление результатов теста",
            "content": csv_data.encode("utf-8").decode("latin1"),  # Base64 encoding
            "sha": sha
        }
        response = requests.put(url, json=data, headers=headers)

        if response.status_code in [200, 201]:
            st.success("Результаты успешно сохранены на GitHub!")
        else:
            st.error("Ошибка при сохранении результатов на GitHub.")
    except Exception as e:
        st.error(f"Произошла ошибка: {e}")
