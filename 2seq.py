

uniq_list = []

numbers = input("Введите последовательность цифр через ',', ';' либо '/': ").replace(';', ',').replace('/', ',').split(',')
numbers_list = [int(elem) for elem in numbers]

for elem in numbers_list:
    if numbers_list.count(elem) == 1:
        uniq_list.append(elem)

print(uniq_list)

