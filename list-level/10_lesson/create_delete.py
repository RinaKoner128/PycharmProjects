#Первое задание
import os

def creat():
    for i in range(1, 10):
        name ='dir_'+str(i)
        os.mkdir(name)

def delete():
    for i in range(1, 10):
        name ='dir_'+str(i)
        os.rmdir(name)
