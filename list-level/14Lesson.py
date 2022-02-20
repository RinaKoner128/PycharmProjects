#Первое задание
obst_1 ={'Груша','Ялоко','Апельсин','Виноград','Слива'}
obst_2 ={'Гранат','Ялоко','Персик','Виноград','Лимон'}
obst=obst_1&obst_2
print(obst)

#Второе задание
int_list=[1, 9, -18, 85, -10, 25, 79, -54, 99, 4, 18, 12]

result_list = [int for int in int_list if int%3==0 and int%4!=0 and int>0]
print(result_list)

#Третье задание
def transform(old_list):
    result=[]
    for i in range(len(old_list)):
        number=old_list[i]
        new_list=number**2 if number>0 else number
        result.append(new_list)
    print(result)

old_list = [1, -3, 4]
print(old_list)
transform(old_list)

#Четвертое задание
def error(int):
    if int==13:
        raise Exception('ValueError')
    int = int ** 2
    print(int)

int = int(input('Введите число от 1 до 100: '))
try:
    error(int)
except:
    print('Введено число 13')
