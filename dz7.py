import random  # модуль з функціями генерації випадкових чисел

search_key = 66

data = {}
# генеруємо рандомне число від 1 до 100, а потім створюємо послідовність від 0 до сгенерованого числа
for i in range(random.randint(1, 100)):
    data[i] = f"item_{i}"  # наповнюємо словник відповідно до послідовності рандомної довжини
if search_key in data.keys():
    print(f"Елемент {search_key}: {data[search_key]}")
else:
    print (f'Помилка: елемент з ключем {search_key} відсутній')
