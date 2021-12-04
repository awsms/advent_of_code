import re

z = []

with open('02.txt', 'r') as file:
    instructions = [i for i in file.readlines()]
    for i in instructions:
        z.append(re.split(' ', i))

for i in range (len(z)):
    z[i][1] = z[i][1].strip()
    z[i][1] = int(z[i][1])

go_up,go_down,go_forward = 0,0,0


for i, j in z:
    if i == 'up':
        go_up += j
    if i == 'down':
        go_down += j
    if i == 'forward':
        go_forward += j
print('go up:',go_up,'\ngo down:',go_down,'\ngo forward:',go_forward)
print('total:',(go_down-go_up)*go_forward)