#Список
list_of_numbers = [8, 45, 1, 60, 9, 65, 90]
#Счётчик
count = 0
#Цикл for
for num in list_of_numbers:
#если число >10, count +1 
    if num > 10:
        count += 1
#Вывод
print(f"Количество чисел, которые больше 10: {count}") 