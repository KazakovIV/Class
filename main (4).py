#1)
while True:
    emal_text = input("введите текст письма")
    if len(emal_text) > 25:
        print("письмо отправленно успешно")
        break
    else:
        print("письмо должно содержать больше 25 символов. попробуйте снова")
        
# 2)
numbers = [10, 6, 4, 30, 9, 1, 9]
for i in numbers:
    if i % 3 == 0:
        print(i)


# 3)
n = int (input(" Введите число: "))

for i in  range(n+1):
    print(i)
