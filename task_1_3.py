for number in range(1, 101):
    if number % 10 == 1 and number % 100 !=11: print(number, 'Процент')
    elif 1 < number % 10 < 5 and not 11 < number % 100 < 15: print(number, 'Процента')
    else: print(number, 'Процентов')