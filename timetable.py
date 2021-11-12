def inp(): # Ввод данных
    Hotp = int(input("Введите часы отправления:"))
    Motp = int(input("Введите минуты отправления:"))
    Hp = int(input("Введите часы в пути:"))
    Mp = int(input("Введите минуты в пути:" ))
    return Hotp, Motp, Hp, Mp

def calc(Hotp, Motp, Hp, Mp): # calculation - вычисление времени
    k = 0
    days = 0
    minutes = Motp + Mp
    if minutes >= 60:
        minutes -= 60
        k += 1
    hours = Hotp + Hp + k
    if Hp < 24:
        if hours >= 24:
            hours -= 24
        days = 0
    else:
        while hours >= 24:
            hours -= 24
            days += 1
    return hours, minutes, days

def out(hours, minutes, days): # Вывод резульата
    if minutes < 10:
        print("Время прибытия:", "%d hours" % hours + " : 0%d minutes" % minutes)
    else:
        print("Время прибытия:", "%d hours" %hours + " : %d minutes" %minutes )
    print("Количество полных суток:", "%d days" %days)
    pass

""" Основная программа """
Hotp, Motp, Hp, Mp = inp()
hours, minutes, days = calc(Hotp, Motp, Hp, Mp)
out(hours, minutes, days)