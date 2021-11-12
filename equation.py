from math import sqrt

def inp(): # Ввод данных
    A = float(input("Введите коэффициент A, не раный 0:"))
    B = float(input("Введите коэффициент B:"))
    C = float(input("Введите коэффициент C:"))
    return A, B, C

def discr(A, B, C):
    discr = B ** 2 - 4 * A * C
    if discr > 0:
        two_x(A, B, discr)
    elif discr == 0:
        one_x(A, B, discr)
    elif discr < 0:
        zero_x()
    pass

def two_x(A, B , discr): # Подсчёт корней уравнения при дискриминанте > 0
    x1 = (-B + sqrt(discr)) / (2 * A)
    x2 = (-B - sqrt(discr)) / (2 * A)
    print("Количество корней: 2")
    print("x1=", "%.5f" % min(x1, x2)) # Вывод корней в формате float с 5-ю знаками после запятой
    print("x2=", "%.5f" % max(x1, x2))
    pass

def one_x(A , B, discr): # Подсчёт корней уравнения при дискриминанте = 0
    x = (-B + sqrt(discr)) / (2 * A)
    print("Количество корней: 1")
    print("x=", "%.5f" % x) # Вывод корней в формате float с 5-ю знаками после запятой
    pass

def zero_x(): # Подсчёт корней уравнения при дискриминанте < 0
    print("Количество корней: 0")
    print("Нет действительных корней")
    pass

""" Основная программа """
A, B, C = inp()
print("Уравнение:")
print("(%.5f)*x^2 + " %A + "(%.5f)*x + " %B + "(%.5f) = 0" %C)
discr(A, B, C)