#1)
time_of_day = input("Какое сейчас время суток? (утро, день или ночь): " )

if time_os_day.lower() == "утро":
    print("Пора вставать")
elif time_os_day.lower() == "день":
    print("Пора учиться")
elif time_os_day.lower() == "ночь":
    print("Пора спать")
else:
    print("Неккоретный ввод")

#2) password ='ibs235'
input_password = input("введите пароль:")
if input_password == password:
    print("пароль правельный")
else:
    print("парольне подходит")



#3)
user_input = input ('Отправится сейчас?(да/нет)')
if user_input == 'да':
    user_input = input('Все ли припасы загруженыв лодку?(да/нет)')
    if user_input == 'да':
        print('В путь!')
    else:
          print('Стоит подготовится лучше')
elif user_input == "нет":
    print("скажи, как будешь готов")
else:
    print("Некорретный ответ.")
#4)
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
operation = input("Что сделать с числами? (* / + -): ")
if operation == "*":
    result = num1 * num2
    print("Результат умножения:", result)
elif operation == "/":
    if num2 == 0:
        print("Ошибка: деление на ноль!")
    else:
        result = num1 / num2
        print("Результат деления:", result)
elif operation == "+":
    result = num1 + num2
    print("Результат сложения:", result)
elif operation == "-":
    result = num1 - num2
    print("Результат вычитания:", result)
else:
    print("Некорректный ввод операции.")

#5)
squares = {
    "B1": "blue",
    "B2": "green",
    "B3": "blue",
    "B4": "green",	
    "B5": None,
    "B6": "green",
    "B7": "blue",
    "B8": "green",
    "C1": "blue",
    "C2": "green",
    "C3": None,
    "C4": "blue",
    "C5": "blue",
    "C6": "blue",
    "C7": "green",
    "C8": "blue",
    "C9": "blue",
    "C10": "green",
    "C11": "green",
    "C12": None,
}
square = input("Введите номер квадрата (например, B1): ")

if square in squares:
    if squares[square] == "green":
        print("В квадрате", square, "сидит зеленый попугай.")
    elif squares[square] == "blue":
        print("В квадрате", square, "сидит синий попугай.")
    else:
        print("В квадрате", square, "никто не сидит.")
else:
    print("Ошибка: такого квадрата нет.")

#6)
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))

if n % k == 0:
    print(n, "кратно", k)
else:
    print(n, "не кратно", k)


