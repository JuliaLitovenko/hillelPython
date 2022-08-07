"""Задача: написати функцію сalculator для двух операндів .

   Деталі:
            * функція приймає три аргумента - лівий операнд, оператор, правий операнд
            * функція повинна повернути результат операції над операндами
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * calculate(2, "+", 2) -> повертає 4
            * calculate("hello world!", "*", 2) -> повертає "hello world!hello world!"
            * calculate(10, ")", 10) -> повертає None
"""


def add(left, right):
    return left + right


def subtract(left, right):
    return left - right


def multiply(left, right):
    return left * right


def divide(left, right):
    return left / right



num1 = float(input("Введіть лівий операнд: "))
num2 = float(input("Введіть правий операнд: "))


print("Операнди: +, -, *, /")
select = input("Виберіть операнд: ")

if select == "+":
    print(num1, "+", num2, "=", add(num1, num2))

elif select == "-":
    print(num1, "-", num2, "=", subtract(num1, num2))

elif select == "*":
    print(num1, "*", num2, "=", multiply(num1, num2))

elif select == "/":
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Невірне введення")