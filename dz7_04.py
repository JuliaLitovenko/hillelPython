# Завдання: написати програму обчислення факторіалу числа.
#           Программа запитує ввод від користувача у циклі
#           (вихід можливий за допомогою Ctrl-C/D)
#
# Факторіал числа: n!
# n! = 1 * 2 * 3 * 4 ... n-1 * n
# 0! = 1
#
# Приклад роботи:
#
# Введіть число для обчислення факторіалу: 5
# 5! == 120
#
# Введіть число для обчислення факторіалу: -5
# Невірний ввод

n = int(input('Введіть число для обчислення факторіалу:'))
fact = 1
if n < 0:
    print('Невірний ввод')
else:
    for i in range(1, n + 1):
        fact = fact * i
    print("Факторіал числа ", n, '! ==', fact)


