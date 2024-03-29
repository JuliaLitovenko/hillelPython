"""Завдання: модіфікувати програму відповідно до коментарів.

Підказки:
 * Получити значення ключу у словнику d["key_name"]
 * створити set з іншого типу set(sequence)
 * сервер Flask'у з першого завдання повинен бути "вімкнутим"(запущеним)
"""
import requests


def main():
    response = requests.get("http://127.0.0.1:5000/class/qautomation")
    data = response.json()

    unique_names = set(data["result"]["students"])  # модіфікувати для отримання тільки унікальних імен у класі
    students = data["result"]["students"]
    print(f"Unique student names in class: {unique_names}")
    print(f"students: {students}")  # відобразити тільки students
    print(f"Ratings: {data.get('result').get('ratings')}")  # відобразити тільки ratings зі словника


if __name__ == "__main__":
    main()
