n = int(input("кол-во элементов: "))
lst = [int(input()) for _ in range(n)]
min_num = lst[0]
for num in lst:
    if num < min_num:
        min_num = num
print(min_num)
