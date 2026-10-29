# 1. Задаем алфавиты (в русском 32 буквы по условию, без 'ё')
eng_lower = "abcdefghijklmnopqrstuvwxyz"
eng_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

print("--- ДОБРО ПОЖАЛОВАТЬ В ШИФРАТОР ЦЕЗАРЯ --- \n")

# 2. Считываем настройки
direction = input("Выберите направление (шифрование / дешифрование): ").lower().strip()
lang = input("Выберите язык алфавита (русский / английский): ").lower().strip()
step = int(input("Введите шаг сдвига (целое число): "))
text = input("Введите текст для обработки:\n")

# Если дешифруем, то сдвиг идет в обратную сторону (назад)
if direction == "дешифрование":
    step = -step


# 3. Функция для обработки одного символа
def transform_char(char, step, lang):
    if lang == "английский":
        if char in eng_lower:
            idx = (eng_lower.index(char) + step) % 26
            return eng_lower[idx]
        elif char in eng_upper:
            idx = (eng_upper.index(char) + step) % 26
            return eng_upper[idx]

    elif lang == "русский":
        if char in rus_lower:
            idx = (rus_lower.index(char) + step) % 32
            return rus_lower[idx]
        elif char in rus_upper:
            idx = (rus_upper.index(char) + step) % 32
            return rus_upper[idx]

    return char  # Если это пробел, цифра или знак препинания — возвращаем без изменений


# 4. Собираем итоговую строку
result = []
for symbol in text:
    result.append(transform_char(symbol, step, lang))

final_text = "".join(result)

print("\n--- РЕЗУЛЬТАТ ОБРАБОТКИ ---")
print(final_text)