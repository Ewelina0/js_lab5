import random

names = ['Damian', 'Ola', 'Barbara', 'Robert', 'Zygmunt','Ewa']
names = [name[0] for name in names]
print('--------------------------List Comprehension 1-----------------------------')

print(names)


i = random.randrange(1, 10)

list = [[random.randrange(1, 10) for element in range(4)] for y in range(5)]
print('--------------------------List Comprehension 2-----------------------------')
print(list)

