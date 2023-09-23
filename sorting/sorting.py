n = int(input("кол-во элементов: "))
lst = [int(input()) for a in range(n)]
for i in range(len(lst)):
    for j in range(i, 0, -1):
        if lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
print(lst)