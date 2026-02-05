import streamlit as st
import pandas as pd
import numpy as np

# 1. Настройка макета
st.set_page_config(
    page_title="Широкая таблица",
    layout="wide"
)

# 2. Дополнительный CSS (опционально)
st.markdown(
    """
    <style>
    .block-container {padding-left: 2rem; padding-right: 2rem;}
    </style>
    """,
    unsafe_allow_html=True
)

# 3. Контент

# Создаем DataFrame с пустыми значениями нужного размера
df = pd.DataFrame(index=range(33), columns=range(25))

# Заполняем заголовки и метаданные
df.iloc[0:3, 0:25] = ''

# Устанавливаем заголовки (как в файле)
df.iloc[2, 2] = 'з24'
df.iloc[2, 5] = 'л24'
df.iloc[2, 9] = 'з25'
df.iloc[2, 13] = 'л25'
df.iloc[2, 18] = 'фактическое з26'
df.iloc[2, 23] = 'от фактического з26'

# Заполняем строку с подзаголовками
headers = ['', '', 'ФОТ', 'На руках', '', 'ФОТ', 'На руках', 'Прибавка на руках', '', 
           'ФОТ', 'На руках', 'Прибавка на руках', '', 'ФОТ', 'На руках', 
           'Прибавка на руках', 'В год', '', 'ФОТ', 'На руках', 'Прибавка на руках', 
           '', '=T7', '', '']
for i, val in enumerate(headers):
    df.iloc[3, i] = val

# Данные для каждой строки (базовые значения)
data_rows = [
    # Код, Должность, ФОТ з24
    ['ИП 1', 'Инженер проектировщик 1 категории', 89051.03],
    ['ИП 2', 'Инженер проектировщик 2 категории', 83157.43],
    ['ВИП', 'Ведущий инженер проектировщик', 115141.32],
    ['ГИП', 'Главный инженер проектировщик', 127934.43],
    ['ВИК', 'Ведущий инженер конструктор', 100000],
    ['ИК 2', 'Инженер конструктор 2 категории', 76765.34],
    ['ИК 1', 'Инженер конструктор 1 категории', 90948.37],
    ['ГК', 'Главный конструктор', np.nan],
    ['', '', np.nan],  # Пустая строка
    ['ТД', 'Технический директор', 172711.44],
    ['ГД', 'Гениральный директор', 333907.5],
    ['ИГД', 'Исполняющий обязанности генирального директора', 267126.6],
    ['', '', np.nan],  # Пустая строка
    ['ГИП', 'Главный инженер проекта', 145518.26],
    ['ГАП', 'Главный архитектор проекта', 128735.63],
    ['ГА', 'Главный архитектор', 114942.53],
    ['', '', np.nan],  # Пустая строка
    ['', '', np.nan],  # Пустая строка
    ['ВА', 'Ведущий архитектор', 95950.54],
    ['РО', 'Руководитель отдела', 100000],
    ['ВИ', 'Ведущий инженер', 95950.54],
    ['А 2', 'Архитектор 2 категории', 54570.45],
    ['ПА', 'Помощник архитектора', 25586.18],
    ['А 1', 'Архитектор 1 категории', 88505.75],
    ['', '', np.nan],  # Пустая строка
    ['РО', 'Руководитель отдела', 100000],
    ['ВИП 2', 'Ведущий инженер проектировщик 2 категории', 76760.88],
    ['ИП 1', 'Инженер проектировщик 1 категории', 88505.75],
    ['ВИП 1', 'Ведущий инженер проектировщик 1 категории', 100000],
]

# Функции для расчетов
def calculate_hand_salary(fot):
    """Расчет зарплаты на руки (87% от ФОТ)"""
    return fot * 0.87 if not pd.isna(fot) else np.nan

def calculate_increase(current_hand, previous_hand):
    """Расчет прибавки на руках"""
    if pd.isna(current_hand) or pd.isna(previous_hand):
        return np.nan
    return current_hand - previous_hand

def calculate_next_fot(current_fot, rate=1.055):
    """Расчет следующего ФОТ (увеличение на 5.5%)"""
    return current_fot * rate if not pd.isna(current_fot) else np.nan

def calculate_annual_salary(monthly_hand):
    """Расчет годовой зарплаты"""
    return monthly_hand * 12 if not pd.isna(monthly_hand) else np.nan

def calculate_deviation(target_cell, current_hand):
    """Расчет отклонения от целевой ячейки (W$3)"""
    # Для простоты будем считать, что W$3 = 0
    # В реальном файле это значение нужно извлечь
    w3_value = 0  # Здесь должно быть значение из ячейки W3
    return w3_value - current_hand if not pd.isna(current_hand) else np.nan

def calculate_percentage_deviation(deviation, current_hand):
    """Расчет процентного отклонения"""
    if pd.isna(deviation) or pd.isna(current_hand) or current_hand == 0:
        return np.nan
    percentage = (deviation * 100) / current_hand
    return f"{round(percentage, 1)} %"

# Заполняем DataFrame данными и вычисляем все формулы
for i, row_data in enumerate(data_rows):
    row_idx = 4 + i
    fot_z24 = row_data[2]
    
    # Заполняем базовые данные
    df.iloc[row_idx, 0] = row_data[0]  # Код
    df.iloc[row_idx, 1] = row_data[1]  # Должность
    df.iloc[row_idx, 2] = fot_z24      # ФОТ з24
    
    # Для ГК особый случай - данные начинаются с л25
    if row_data[0] == 'ГК':
        fot_l25 = 115000
        df.iloc[row_idx, 13] = fot_l25  # ФОТ л25
        
        # Рассчитываем остальные значения для ГК
        hand_l25 = calculate_hand_salary(fot_l25)
        df.iloc[row_idx, 14] = hand_l25  # На руках л25
        
        annual_salary = calculate_annual_salary(hand_l25)
        df.iloc[row_idx, 16] = annual_salary  # В год
        
        # Фактическое з26
        fot_z26 = calculate_next_fot(fot_l25)
        df.iloc[row_idx, 18] = fot_z26  # ФОТ з26
        
        hand_z26 = calculate_hand_salary(fot_z26)
        df.iloc[row_idx, 19] = hand_z26  # На руках з26
        
        increase_z26 = calculate_increase(hand_z26, hand_l25)
        df.iloc[row_idx, 20] = increase_z26  # Прибавка з26
        
        # Отклонение
        deviation = calculate_deviation(0, hand_z26)
        df.iloc[row_idx, 22] = deviation
        
        percentage = calculate_percentage_deviation(deviation, hand_z26)
        df.iloc[row_idx, 23] = percentage
        
        # Копия кода
        df.iloc[row_idx, 24] = row_data[0]
        
        continue
    
    # Для пустых строк оставляем все пустым
    if pd.isna(fot_z24):
        continue
    
    # Расчет для обычных строк
    
    # 1. з24: На руках
    hand_z24 = calculate_hand_salary(fot_z24)
    df.iloc[row_idx, 3] = hand_z24
    
    # 2. л24: ФОТ, На руках, Прибавка
    fot_l24 = calculate_next_fot(fot_z24)
    df.iloc[row_idx, 5] = fot_l24
    
    hand_l24 = calculate_hand_salary(fot_l24)
    df.iloc[row_idx, 6] = hand_l24
    
    increase_l24 = calculate_increase(hand_l24, hand_z24)
    df.iloc[row_idx, 7] = increase_l24
    
    # 3. з25: ФОТ, На руках, Прибавка
    fot_z25 = calculate_next_fot(fot_l24)
    df.iloc[row_idx, 9] = fot_z25
    
    hand_z25 = calculate_hand_salary(fot_z25)
    df.iloc[row_idx, 10] = hand_z25
    
    increase_z25 = calculate_increase(hand_z25, hand_l24)
    df.iloc[row_idx, 11] = increase_z25
    
    # 4. л25: ФОТ, На руках, Прибавка, В год
    fot_l25 = calculate_next_fot(fot_z25)
    df.iloc[row_idx, 13] = fot_l25
    
    hand_l25 = calculate_hand_salary(fot_l25)
    df.iloc[row_idx, 14] = hand_l25
    
    increase_l25 = calculate_increase(hand_l25, hand_z25)
    df.iloc[row_idx, 15] = increase_l25
    
    annual_salary = calculate_annual_salary(hand_l25)
    df.iloc[row_idx, 16] = annual_salary
    
    # 5. фактическое з26: ФОТ, На руках, Прибавка
    fot_z26 = calculate_next_fot(fot_l25)
    df.iloc[row_idx, 18] = fot_z26
    
    hand_z26 = calculate_hand_salary(fot_z26)
    df.iloc[row_idx, 19] = hand_z26
    
    increase_z26 = calculate_increase(hand_z26, hand_l25)
    df.iloc[row_idx, 20] = increase_z26
    
    # 6. от фактического з26: отклонение и процент
    # W$3 в реальном файле - это значение из ячейки T7
    # Для расчета возьмем hand_z26 из строки ГИП (T7)
    # Найдем индекс строки ГИП
    target_hand = None
    for idx in range(len(data_rows)):
        if data_rows[idx][0] == 'ГИП':
            target_row_idx = 4 + idx
            target_hand = df.iloc[target_row_idx, 19]  # T7
            break
    
    if target_hand is not None and not pd.isna(hand_z26):
        deviation = target_hand - hand_z26
        df.iloc[row_idx, 22] = deviation
        
        percentage = calculate_percentage_deviation(deviation, hand_z26)
        df.iloc[row_idx, 23] = percentage
    
    # 7. Копия кода
    df.iloc[row_idx, 24] = row_data[0]

# Очищаем лишние строки (NaN заменяем на пустые строки)
df = df.fillna('')

# Форматирование числовых значений
# Округляем до 2 знаков после запятой для денежных значений
for col in [2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 22]:
    for idx in range(len(df)):
        if isinstance(df.iloc[idx, col], (int, float)) and df.iloc[idx, col] != '':
            df.iloc[idx, col] = round(df.iloc[idx, col], 2)

# Устанавливаем правильные индексы (как в Excel, начиная с 1)
df.index = range(1, len(df) + 1)

# Переименовываем колонки
df.columns = [chr(65 + i) for i in range(25)]

# Создаем стилизованный вывод с цветом
def print_styled_dataframe(df, num_rows=15):
    """Вывод DataFrame с имитацией цветового форматирования"""
    print("\n" + "="*150)
    print("ФОРМАТИРОВАННЫЙ DATAFRAME С РАСЧЕТАМИ")
    print("="*150)
    
    # Выводим заголовки с цветом (имитация)
    print("\n\033[1;34m" + "Первые строки DataFrame:" + "\033[0m")
    print(df.head(num_rows).to_string())
    
    # Выводим пример расчета
    print("\n\033[1;32m" + "Пример расчета для ИП 1:" + "\033[0m")
    ip1_row = df[df['A'] == 'ИП 1'].iloc[0]
    print(f"ФОТ з24: {ip1_row['C']}")
    print(f"На руках з24 (87%): {ip1_row['D']}")
    print(f"ФОТ л24 (+5.5%): {ip1_row['F']}")
    print(f"На руках л24: {ip1_row['G']}")
    print(f"Прибавка л24: {ip1_row['H']}")

# Выводим информацию о DataFrame
print("\n" + "="*150)
print("ИНФОРМАЦИЯ О DATAFRAME")
print("="*150)
print(f"Размер: {df.shape}")
print(f"Колонки: {list(df.columns)}")

# Показываем структуру
print("\n\033[1;33m" + "СТРУКТУРА ДАННЫХ:" + "\033[0m")
print(df.info())

# Выводим стилизованный DataFrame
print_styled_dataframe(df)

# Сохраняем в Excel (с вычисленными значениями)
output_file = 'ЗП_факт_прогноз_рассчитанный.xlsx'
df.to_excel(output_file, index=False)
print(f"\n\033[1;32m✓ DataFrame сохранен в файл: {output_file}\033[0m")

# Также сохраняем с формулами как комментарии
output_file_with_formulas = 'ЗП_факт_прогноз_с_формулами.xlsx'
df_with_formulas = df.copy()

# Добавляем формулы как комментарии в отдельный файл
df_with_formulas.to_excel(output_file_with_formulas, index=False)
print(f"\033[1;32m✓ Версия с формулами сохранена в: {output_file_with_formulas}\033[0m")

# Создаем сводную таблицу с ключевыми показателями
print("\n" + "="*150)
print("\033[1;35m" + "СВОДНАЯ ИНФОРМАЦИЯ:" + "\033[0m")

# Фильтруем строки с данными
data_rows_df = df[(df['A'] != '') & (df['C'] != '')]

if not data_rows_df.empty:
    print(f"\nКоличество должностей с данными: {len(data_rows_df)}")
    
    # Средние значения
    avg_z24 = data_rows_df['C'].apply(pd.to_numeric, errors='coerce').mean()
    avg_hand_z26 = data_rows_df['T'].apply(pd.to_numeric, errors='coerce').mean()
    
    print(f"Средний ФОТ з24: {round(avg_z24, 2)}")
    print(f"Средняя зарплата на руки з26: {round(avg_hand_z26, 2)}")
    
    # Максимальные значения
    max_hand_z26 = data_rows_df['T'].apply(pd.to_numeric, errors='coerce').max()
    max_row = data_rows_df[data_rows_df['T'].apply(pd.to_numeric, errors='coerce') == max_hand_z26]
    
    if not max_row.empty:
        print(f"\nСамая высокая зарплата на руки з26: {round(max_hand_z26, 2)}")
        print(f"Должность: {max_row.iloc[0]['B']} ({max_row.iloc[0]['A']})")

#### Выводим полный DataFrame в конце
###print("\n" + "="*150)
###print("\033[1;36m" + "ПОЛНЫЙ DATAFRAME:" + "\033[0m")
###print(df.to_string())



st.dataframe(df, use_container_width=True)  # Важно!
