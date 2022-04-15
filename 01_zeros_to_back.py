integers = input().split(', ')
integers_copy = list(map(int, integers))

for i in range(len(integers_copy)-1, -1, -1):
    if integers_copy[i] == 0:
        integers_copy.pop(i)
        integers_copy.append(0)

print(integers_copy)
