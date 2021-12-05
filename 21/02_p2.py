'''
--- Day 2: Dive! ---

--- Part Two ---        '''

import re

z = []

with open('02.txt', 'r') as file:
    instructions = [str(n.strip()) for n in file.readlines()]
    for i in instructions:
        z.append(re.split(' ', i))

for i in range (len(z)):
#     z[i][1] = z[i][1].strip()
    z[i][1] = int(z[i][1])

aim,go_down,go_forward = 0,0,0

for i, j in z:
    if i == 'up':
        aim -= j
    if i == 'down':
        aim += j
    if i == 'forward':
        go_forward += j
        go_down += j * aim
# print('go up:',go_up,'\ngo down:',go_down,'\ngo forward:',go_forward)
# print('total:',(go_down-go_up)*go_forward)
print('aim:',aim,'\ngo down:',go_down,'\ngo forward:',go_forward)
print('final distance:',go_down*go_forward)