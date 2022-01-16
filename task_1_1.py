while True:
    sec = int(input('Введите число в секнудах: '))
    day = sec // 86400
    sec -= day * 86400
    hour = sec // 3600
    sec %= 3600
    sec = sec % (24 * 3600)
    minute = sec // 60
    sec %= 60
    if day == 1:
        print(day, 'день', hour, 'час', minute, 'мин', sec, 'сек')
    elif day > 1 and day < 5:
        print(day, 'дня', hour, 'час', minute, 'мин', sec, 'сек')
    else:
        print(day, 'дней', hour, 'час', minute, 'мин', sec, 'сек')