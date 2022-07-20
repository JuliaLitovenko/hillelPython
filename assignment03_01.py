#!/usr/bin/python3

# Assignment 03-01
#
# Завдання: задати формулу обчислення відстані L (замінити None на математичну формулу
#           наведену нижче) - подальщий код приймає відповідне рішення - належить чи ні
#           координата (Px, Py) до кільця (з центром у Cx, Cy та радіусами r1, r2).
#
# Варіанти виводу на екран:
#
#      1. "Координата (Px, Py) належить кільцю за центром у (Cx, Cy) та радіусами r1 = R1, r2 = R2"
#      2. "Координата (Px, Py) не належить кільцю за центром у (Cx, Cy) та радіусами r1 = R1, r2 = R2"
#
# Формула відстані від заданої координати та координати центру кола:
#
#      L = sqrt((Px-Cx)^2 + (Py-Cy)^2),
#
#      якщо умова - r1 < L < r2 - виконується - точка належить кільцю,
#      інакше - ні
#
#      де:
#          L - відстань між двома точками з коордінатами
#          Px, Py - координата точки
#          Cx, Cy - координата центру кола r1 та r2
#          r1, r2 - радіус внутрішньго/зовнішнього кола
#
# Приклад приналежності:
#
# Cx = 0, Cy = 0
# r1 = 3
# r2 = 7
# Px = 4, Py = 5
#
# L = sqrt((4-0)^2 + (5-0)^2) == 6.4
#
# "Координата (4, 5) належить кільцю з центром у (0, 0) та радіусами r1 = 3, r2 = 7"
#
# Підказка:
#     * sqrt - через пайтонівські аріфметичні операції: N**0.5, 4**0.5 == 2, 16**0.5 == 4...
import math
Px = int(input("Введіть Px: "))  # зчитування значення від користувача та конвертація у число (int)
Py = int(input("Введіть Py: "))
Cx = int(input("Введіть Сx: "))
Cy = int(input("Введіть Сy: "))
r1 = int(input("Введіть r1: "))
r2 = int(input("Введіть r2: "))


L = math.sqrt((Px-Cx)**2 + (Py-Cy)**2)

result = "не належить"
if r1 < L < r2:
   result = "належить"

print(f"Координата ({Px}, {Py}) {result} кільцю за центром у ({Cx}, {Cy}) та радіусами r1 = {r1}, r2 = {r2}")

