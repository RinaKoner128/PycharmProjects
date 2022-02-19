#Второе задание
import random

def get_list(list):
    if len(list) == 0:
        print('None')
    else:
        print(random.choice(list))
