
#Первое задание
def registration(name, age, city):
    print(name,',', age, 'год. Проживает в городе',city)
print('Первое задание')
name=input('Ваше имя: ')
age=input('Ваш возраст: ')
city=input('Город Вашего проживания: ')
registration(name, age, city)

#Второе задание
def max_value(user_list):
    print(max(user_list))
user_list = input('Введите числа через запятую: ')
user_list=user_list.split(',')
for i, item in enumerate(user_list):
    user_list[i] = int(item)
max_value(user_list)

#Третье задание
def attack(player, enemy):
    def new_damage():
        armor = 1.2
        player['damage'] = player['damage']/ armor
        enemy['damage'] = enemy['damage']/ armor
    new_damage()
    player['health'] = player['health'] - enemy['damage']
    enemy['health'] = enemy['health'] - player['damage']
    return player, enemy

player ={
    'name':'Игрок',
    'health':120,
    'damage':60}
enemy ={
    'name':'Злодей',
    'health':120,
    'damage':40}

player['name']=input('Введите имя Игрока 1')
enemy['name']=input('Введите имя Игрока 2')
change=input('Напишите "удар" или "выход", чтобы ударить противника или выйти из игры')
while change=='удар':
    attack(player, enemy)
    print(player['name'],'=',round(player['health']),enemy['name'],'=',round(enemy['health']))
    change = input('Напишите "удар" или "выход", чтобы ударить противника или выйти из игры')
print('Игра окончена! Игрок',player['name'],'осталось', round(player['health']), 'единиц жизни. Игрок',enemy['name'],'осталось', round(enemy['health']), 'единиц жизни')

