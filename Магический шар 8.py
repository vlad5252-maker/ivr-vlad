# print(input().capitalize())
# s = input().split("\\")
# print("True" if s[4][0].lower().startswith(("а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я")) else "False")
# import keyword
# n, m = int(input()), int(input())
# print(keyword.kwlist[n: m])
# import string
# remove_digits = str.maketrans("", "", string.digits)
# print("Интересный факт: если вы умножите свой возраст на 7, "
#       "а затем умножите полученное число на 1443, результат "
#       "будет представлять ваш возраст, написанный 3 раза подряд".translate(remove_digits))

# print("Привет, "
#       "мир!")
# s = input()
# s.translate(str.maketrans(("б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с," "т", "ф", "х", "ц", "ч", "ш", "щ"), "г", "й"))
# s.translate(str.maketrans({"БВГДЖЗКЛМНПРСТФХЦЧШЩ"}, "Г", "Й"))
# print(s)
# text = input().lower()
# word = input().lower()
# cnt = 0
# while word in text:
#     text = text.replace(word, "", 1)
#     cnt += 1
# print(cnt)
# import string
# k = ''
# s = input()
# l = []
# print(string.ascii_letters)
# for i in s:
#     while i in string.ascii_letters:
#         k += i
#     l.append(k)
# print(l)

# s = input()
# i = 0
# k = ''
# while s[i] in rus_letters:
#     k += s[i]
#     i += 1
# print(k)
# rus_lowercase = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
# rus_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
# rus_letters = rus_uppercase + rus_lowercase
# s = input().split()
# cnt = 0
# for i in s:
#     if i[0] in rus_letters:
#         cnt += 1
# print(cnt)
from random import choice
answers = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
print("Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.\n")
name = input("Как вас зовут, друг? ")
print(f"Привет {name}")
while True:
    quest = input("Задавайте свой вопрос ")
    answer = choice(answers)
    print(answer)
    x = input("Хотите ли вы задать еще вопрос? (да/нет)\n")
    if x.lower().strip() == "да":
        continue
    elif x.lower().strip() == "нет":
        print("Возвращайся, если возникнут вопросы!")
        break