def inp(): # Ввод переменных
    a = float(input("Введите сторону a:"))
    b = float(input("Введите сторону b:"))
    c = float(input("Введите сторону c:"))
    return a, b, c

def check(a, b, c): # Проверка на существование треугольника
    if (a + b > c):
        if (b + c > a):
            if (a + c > b):
                return True
    else:
        return False

def kind(a, b, c): # Определение вида треугольника
    if a == b == c:
        i = 1
    elif (a == b) or (b == c) or (a == c):
        i = 2
    else:
        i = 3
    return i

def out(i): # Вывод результата
    if i == 0:
        print("Треугольник не существует")
    elif i == 1:
        print("Треугольник равносторонний")
    elif i == 2:
        print("Треугольник равнобедренный")
    elif i == 3:
        print("Треугольник общего вида")
    pass

"""Основная программа"""
a, b, c = inp()
if check(a, b, c) == True:
    i = kind(a, b, c)
else:
    i = 0
out(i)