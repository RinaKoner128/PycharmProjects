import random
min_number=1
max_number=100
number = random.randint(min_number, max_number)
print('Добби думает, что хозяин загадал число ', number)
user_helps = input('Хозяин, дай Добби подсказку, число больше или меньше? Или Добби угадал?')
while user_helps !='верно':
    if user_helps =='больше':
        min_number=number+1
        number=random.randint(min_number, max_number)
        print('Тогда ', number)
        user_helps = input('Хозяин, а сейчас Добби угадал?')
    elif user_helps =='меньше':
        max_number = number - 1
        number = random.randint(min_number, max_number)
        print('Тогда ', number)
        user_helps = input('Хозяин, а сейчас Добби угадал?')
print('Ура, Добби свободен!', number, 'Правильное число')