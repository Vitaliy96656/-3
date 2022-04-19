import random

famous_people_data = {
    'Mikhailo Lomonosov': '19.11.1711',
    'Vladimir Lenin': '22.04.1870',
    'Ivan Pavlov': '26.09.1849',
    'Ivan Sechenov': '13.08.1829',
    'Piotr Anokhin': '26.01.1898',
    'Zigmund Freud': '06.05.1856',
    'Zoya Kosmodemyanskaya': '13.09.1923',
    'Sergey Korolev': '12.01.1907',
    'Evgeniy Shvartz': '21.10.1896',
    'Iisus Christos': '01.01.0001',
}
month_names = [
    '',
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря',
]
day_names = [
    '',
    'первого',
    'второго',
    'третьего',
    'четвертого',
    'пятого',
    'шестого',
    'седьмого',
    'восьмого',
    'девятого',
    'десятого',
    'одиннадцатого',
    'двенадцатого',
    'тринадцатого',
    'четырнадцатого',
    'пятнадцатого',
    'шестнадцатого',
    'семнадцатого',
    'восемнадцатого',
    'девятнадцатого',
    'двадцатого',
    'двадцать первого',
    'двадцать второго',
    'двадцать третьего',
    'двадцать четвертого',
    'двадцать пятого',
    'двадцать шестого',
    'двадцать седьмого',
    'двадцать восьмого',
    'двадцать деватого',
    'тридцатого',
    'тридцать первого',
]
next_round = 'y'
while next_round == 'y':
    hit = 0
    lose = 0
    random_five_famous_names = random.sample(famous_people_data.keys(), 5)
    print(random_five_famous_names)
    for name in random_five_famous_names:
        # проверка корректности ввода
        correct_input = False
        while not correct_input:
            answer = input(f'Введите дату рождения для {name} в формате dd.mm.yyyy: ')
            if len(answer) == 10:
                if '.' in answer:
                    if answer.count('.') == 2:
                        datas = answer.split('.')
                        if len(datas[0]) == len(datas[1]) == 2 and len(datas[2]) == 4:
                            if datas[0].isdigit() and datas[1].isdigit() and datas[2].isdigit():
                                correct_input = True
                            else:
                                print('Введены НЕ числа')
                        else:
                            print(f'Неверная длина чисел даты рождения!')
                    else:
                        print(f'В дате должно быть ровно две разделительные точки!')
                else:
                    print(f'Дата должна быть разделена точками!!!')
            else:
                print(f'Неверный формат даты рождения! {name} недоволен!!!')
        if answer == famous_people_data[name]:
            hit += 1
            print('Верно!)')
        else:
            lose += 1
            true_datas = famous_people_data[name].split('.')
            print(
                f'Вы ошиблись... {name} родился {day_names[int(true_datas[0])]} {month_names[int(true_datas[1])]} {int(true_datas[2])} года')

    hit_percent = (100 * hit // (hit + lose))
    lose_percent = (100 * lose // (hit + lose))
    print(f'Верно угадано: {hit} ({hit_percent}%), ошибок: {lose} ({lose_percent}%)!\n')
