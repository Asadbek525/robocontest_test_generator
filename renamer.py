exampleTestCount = int(input())
att_messages = input().split()
attempts = len(att_messages)
att_times = list(map(int, input().split()))
att_times = list(att_times)


penalty = 0
for j in range(attempts):
    if att_messages[j] == 'ACC':
        penalty += att_times[j] - 1
        print(penalty)
        exit()
    if att_messages[j].count('#') > 0 and int(att_messages[j].split('#')[1]) > exampleTestCount:
        penalty += 5

print(f'{0}')
