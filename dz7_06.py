"""Задача: написати функцію пошуку елемента у послідовності.

   Деталі:
            * функція приймає два аргумента - послідовність та елемен
            * функція повинна повернути індекс елемента у послідовності
              або -1 якщо не знайдено
            * це аналог функції str.find, list.index
            * написати якийсь код який надає пару прикладів використування

    Приклад:
            * search_linearly([1, 8, 7, 33, 9, 2], 8) -> повертає 1
            * search_linearly("hello world!", "!") -> повертає 11
            * search_linearly(tuple(range(10)), 10) -> повертає -1
"""

seq,elem = "hello world!", "!"

def search_linearly(a,b):
        n = 0
        for i in a:
            if i == b:
                break
            n += 1
        if (n + 1) > len(a):
            n = -1
        return n

print(search_linearly(seq,elem))

