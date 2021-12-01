'''
--- Day 1: Sonar Sweep ---

--- Part Two ---        '''

count = 0
with open('01.txt', 'r') as file:
    lines = [int(i) for i in file.readlines()]
    for i in range(len(lines)):
        if lines[i] > lines[i-3]:
            count += 1
print(count)