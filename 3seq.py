
numbers_seq_1 = input("Введите первую последовательность цифр через ',', ';' либо '/': ").replace(';', ',').replace('/', ',').split(',')
numbers_list_1 = [int(elem) for elem in numbers_seq_1]

numbers_seq_2 = input("Введите вторую последовательность цифр через ',', ';' либо '/': ").replace(';', ',').replace('/', ',').split(',')
numbers_list_2 = [int(elem) for elem in numbers_seq_2]

for num in numbers_list_1[::-1]:
    if num in numbers_list_2:
        numbers_list_1.remove(num)

print(f'Результат: {numbers_list_1}')