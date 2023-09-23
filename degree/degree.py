number = int(input('Введите число: '))
degree = int(input('Введите степень: '))
for i in range(1, degree):
    number = number*number
print(number)