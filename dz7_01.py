# Є словник з ключами-строками та елементами-списками строк, наприклад:
#
data = {
	'colors': ['red', 'green', 'blue', 'purple'],
  	'fruits': ['pineapple', 'orange', 'banana'],
  	'clothes': ['coat', 'tshirt']
}
#
# Завдання: перебудувати словник таким чином що
#           його значення стануть ключами значенням котрих буде їхній
#           ключ з початкового словника. Вирішити за допомогою dict
#           comprehensions.

data = {
	'colors': ['red', 'green', 'blue', 'purple'],
  	'fruits': ['pineapple', 'orange', 'banana'],
  	'clothes': ['coat', 'tshirt']
}

new_list= {k:v for v in data.keys() for k in data[v]}
print(new_list)