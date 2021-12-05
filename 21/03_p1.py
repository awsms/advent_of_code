'''
--- Day 3: Binary Diagnostic ---

--- Part One ---        '''

import re

gamma_rate = []
epsilon_rate = []
begins_with_null = []
begins_with_one = []

with open('03.txt', 'r') as file:
    instructions = [str(n.strip()) for n in file.readlines()]
    for f in instructions:
        if re.match('^0',f):
            begins_with_null.append(f)
        else:
            begins_with_one.append(f)

# for i in range (len(begins_with_one)):
#     begins_with_one[i] = begins_with_one[i].strip()
#     begins_with_one[i] = str(begins_with_one[i])
# for i in range (len(begins_with_null)):
#     begins_with_null[i] = begins_with_null[i].strip()
#     begins_with_null[i] = str(begins_with_null[i])

if (len(begins_with_one)) > (len(begins_with_null)):
    epsilon_rate = begins_with_one
else:
    gamma_rate = begins_with_null


# def moyenne_des_valeurs(list):
#     nb_de_zeros = 0
#     nb_de_huns = 0
#     # for f,j in zip(list, range(len(list[0]))):
#     #     print(i)
#     #     print(j)
#     #     if list[j][0] == '0':
#     #         nb_de_zeros -= 1
#     #     else:
#     #         nb_de_zeros += 1
#     # print(nb_de_zeros)
#     count = 0
#     for i in list:
#         # print('i:',i,'j:',j)
#         for j in range(12):
#             if list[count][j] == '0':
#                 nb_de_zeros += 1
#             else:
#                 nb_de_huns += 1
#         count +=1
#         # for f,j

# moyenne_des_valeurs(gamma_rate)

# for i in range(len(gamma_rate)):
#     print(gamma_rate[i])



# for f in gamma_rate:
#     print(f)

# print(len(gamma_rate))
# print(len(gamma_rate[1]))
# print(len(gamma_rate[0]))

# for i, element in enumerate(gamma_rate):
#     print('working with index:',i)
#     print(element)

nb_de_zeros = 0
nb_de_huns = 0
count = 0
# for i in gamma_rate:
#     # print('i:',i,'j:',j)
#     for j in range(12):
#         print('i:',i,'j:',j,'gamma_rate[count][j]:',gamma_rate[count][j])
#         # if gamma_rate[count][j] == '0':
#         #     nb_de_zeros += 1
#         # else:
#         #     nb_de_huns += 1
#     count +=1
#     print(nb_de_huns)
#     print(nb_de_zeros)
count = 0
gamma_rate_moyennes = []
for j in range(12):
    for i in gamma_rate:
        print('i:',i,'j:',j,'gamma_rate[count][j]:',gamma_rate[count][j])
        if i[count][j] == '0':
            nb_de_zeros += 1
        else:
            nb_de_huns += 1
        print(nb_de_huns,nb_de_zeros)
    count +=1