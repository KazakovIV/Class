my_name = "Иван"
my_age = 30

user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? "))

if user_name == my_name:
    print("У нас одинаковые имена")
    if user_age == my_age:
        print("А ещё у нас одинаковый возраст")
    else:
        print(f"Приятно познакомится, {user_name}!")
else: 
    print(f"Приятно познакомится,{user_name}!")
    
if user_age > my_age:
    print("Ты старше, чем я.")
elif user_age == my_age:
    print("Возраст у нас одинаковый")
else: 
    print("Ты младше чем я")

