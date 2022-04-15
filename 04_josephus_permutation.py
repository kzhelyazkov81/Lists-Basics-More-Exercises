members = input().split(' ')
k = int(input())
executed_list = []
executed_index = k - 1

while len(members) > 0:
    if executed_index >= len(members):
        executed_index -= len(members)
        continue
    executed = members[executed_index]
    executed_list.append(int(executed))
    members.pop(executed_index)
    executed_index += k - 1

result = str(executed_list).replace(' ', '')
print(result)
