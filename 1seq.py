
a = []
y = int(input("Введите количество элементов: "))
for i in range(y):
    a.append(int(input(f"введите {1+i} элемент: ")))
    a.sort()
print(a)