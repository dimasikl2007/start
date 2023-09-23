n = int(input("кол-во элементов: "))
lst = [int(input()) for _ in range(n)]
max_num = lst[0]
for num in lst:
    if num > max_num:
        max_num = num
print(max_num)