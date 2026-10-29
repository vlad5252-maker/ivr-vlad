from random import choice

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

print("--- ДОБРО ПОЖАЛОВАТЬ В ГЕНЕРАТОР ПАРОЛЕЙ --- \n")

# 1. Считываем настройки
n = int(input("Введите количество паролей для генерации: "))
length = int(input("Введите длину пароля: "))

add_digits = input(f"Включать ли цифры '{digits}'? (да/нет): ").lower().strip() == "да"
add_lowercase = input(f"Включать ли прописные (строчные) буквы? (да/нет): ").lower().strip() == "да"
add_uppercase = input(f"Включать ли заглавные буквы? (да/нет): ").lower().strip() == "да"
add_punctuation = input(f"Включать ли символы '{punctuation}'? (да/нет): ").lower().strip() == "да"
remove_ambiguous = input("Исключать ли неоднозначные символы 'il1Lo0O'? (да/нет): ").lower().strip() == "да"

# 2. Собираем единый пул доступных символов (chars)
chars = ""
if add_digits:
    chars += digits
if add_lowercase:
    chars += lowercase_letters
if add_uppercase:
    chars += uppercase_letters
if add_punctuation:
    chars += punctuation

# 3. Если нужно, выкидываем неоднозначные символы
if remove_ambiguous:
    chars = "".join(c for c in chars if c not in "il1Lo0O")
def generate_password():
    print("\n--- ВАШИ СГЕНЕРИРОВАННЫЕ ПАРОЛИ ---")

    # 4. Проверяем, что пул символов не пустой
    if chars == "":
        print("Ошибка: вы не выбрали ни один тип символов для генерации!")
    else:
        # Генерируем n паролей
        for _ in range(n):
            # Собираем пароль по одному случайному символу из пула chars
            password = "".join(choice(chars) for _ in range(length))
            print(password)
generate_password()