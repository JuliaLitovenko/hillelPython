# зчитати ввод від користувача - речення (текст) - та порахувати кожне слово у реченні,
# кількість разів воно зустрічається у реченні. Також порахувати статистику використаних
# літер. Для зберігання статистик використати словники.
#
# Підказки:
# * input
# * str.split
# * for word in sequence
# * if key in dict
# * if key not in dict


text = input('Введіть текст: ')
word= text.split()
amount = len(word)
count_words={}

for w in word:
    if w in text:
     count_words[w]= word.count(w)


letters ={}
for l in text:
    if l in text:
        if l.isalpha():
            letters[l]= text.count(l)


print(f'Кiлькiсть слiв у реченнi: {amount}')
print(f'Статистика слів у реченні : {count_words}')
print(f'Кількість літер у реченні : {letters}')


