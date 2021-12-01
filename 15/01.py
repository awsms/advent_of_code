'''
--- Day 1: Not Quite Lisp ---
'''

current_floor = 0
go_up = '('
go_down = ')'

with open('01.txt', encoding='utf-8', mode='r') as file:
    path = [str(i) for i in file.readline()]
    for char in (path):
        # for i in range (len(path)):
        if char == go_up:
            current_floor += 1
        elif char == go_down:
            current_floor -= 1
        else:
            break
print(current_floor)