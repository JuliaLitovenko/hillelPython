


text = input('Введіть текст:')
user_letter = input('Введіть літеру:')
y = len(user_letter)
count = text.count(user_letter)

if len(user_letter) > 1:
   print('Введіть лише одну букву')



if  count > 0 and count < 10:
    print(f'Строка містить літеру "{user_letter}" до 10 разів' )
elif count >=10 and  count <= 20:
    print (f'Строка містить літеру "{user_letter}" до 20 разів' )
elif  count >= 20 :
   print(f'Строка містить літеру "{user_letter}" більше 20 разів')
else:
    print ("Такої літери в тексті не виявлено")
