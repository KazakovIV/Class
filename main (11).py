
correct_password = "Password123"
user_password = input("Введите пароль: ")
access_level = None
for _ in range(3): 
    if user_password == correct_password:
        access_level = "Полный доступ"
        break
    else:
        print("Неверный пароль, попробуйте еще раз.")
        user_password = input("Введите пароль еще раз: ")
if access_level:
    print(f"Доступ: {access_level}")
else:
    print("Превышено количество попыток. Доступ заблокирован.")

 