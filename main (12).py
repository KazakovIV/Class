#1)
todo_list = ['Приготовить завтрак', "Сходить в мазагин", "Выполнить домашнее задание"]
for item in todo_list:
    print(item)   
todo_list.append("Погулять с собакой")
print(todo_list)
for item in todo_list:
    print(item)


#2)
shopping_list = ["Яблоки", "Молоко", "Хлеб", "Мясо", "Яйца"]
for item in shopping_list:
    if item == "Молоко" or item == "Яйца":
        print(f"Купить {item} в количестве 2 шт.")
    else:
        print(f"Купить {item} в количестве 1 шт.")
