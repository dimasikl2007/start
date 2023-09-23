b = open('lst.txt', 'r')

c = b.readlines()
regels = list(c)
print(regels)

max = 0
for line in b.readlines():
  num = int(line.split(",")[0])
  print(num)
  if (max < num):
    max = num


print(max)
# Close file
b.close()