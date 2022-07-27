


str = input('Введіть текст:')
user_letter = input('Введіть літеру:')
y = len(user_letter)
count = str.count(user_letter)

if len(user_letter) > 1:
   print('Введіть лише одну букву')
else:
    pass



if user_letter in str and count <= 10:
    print(f'Строка містить літеру "{user_letter}" до 10 разів' )
elif user_letter in str and (count >=10) and  (count <= 20):
    print (f'Строка містить літеру "{user_letter}" до 20 разів' )
elif user_letter in str and count >= 20 :
   print(f'Строка містить літеру "{user_letter}" більше 20 разів')
else:
    print ("Такої літери в тексті не виявлено")
