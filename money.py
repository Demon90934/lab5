def inp(): # Ввод данных
    kopecks = int(input("Введите число копеек:"))
    return kopecks

def calc(kopecks): # Подсчёт рублей и копеек
    rubles = 0
    while kopecks >= 100:
        kopecks -= 100
        rubles += 1
    return rubles, kopecks

def out_r(rubles): # Вывод рублей. Слово "рубль" согласовано с числительными
    if rubles == 0:
        return None
    else:
        if (rubles % 10 == 2) or (rubles % 10 == 3) or (rubles % 10 == 4):
            if (rubles % 100 != 12) and (rubles % 100 != 13) and (rubles % 100 != 14):
                print("%d РУБЛЯ" %rubles)
            else:
                print("%d РУБЛЕЙ" %rubles)
        elif rubles % 10 == 1:
            if rubles % 100 != 11:
                print("%d РУБЛЬ" %rubles)
            else:
                print("%d РУБЛЕЙ" % rubles)
        else:
            print("%d РУБЛЕЙ" % rubles)
    pass

def out_k(kopecks): # Вывод копеек. Слово "копейка" согласовано с числительными
    if kopecks == 0:
        return None
    else:
        if (kopecks % 10 == 2) or (kopecks % 10 == 3) or (kopecks % 10 == 4):
            if (kopecks % 100 != 12) and (kopecks % 100 != 13) and (kopecks % 100 != 14):
                print("%d КОПЕЙКИ" %kopecks)
            else:
                print("%d КОПЕЕК" %kopecks)
        elif kopecks % 10 == 1:
            if kopecks % 100 != 11:
                print("%d КОПЕЙКА" %kopecks)
            else:
                print("%d КОПЕЕК" %kopecks)
        else:
            print("%d КОПЕЕК" %kopecks)
    pass

""" Основная программа """
kopecks = inp()
rubles, kopecks = calc(kopecks)
out_r(rubles)
out_k(kopecks)