# start
import random
from operator import ifloordiv

# a
list_95_105: list[int] = [i for i in range(95, 106)]
print('list_95_105:', list_95_105)
# b
list_10_20: list[int] = [i for i in range(10, 21, 2)]
print('list_10_20:', list_10_20)
# c
list_c: list[int] = [random.randint(0, 100) for _ in range(5)]
print('list_c', list_c)
# d
list_random: list[int] = [random.randint(1, 100) for _ in range(10)]
print('list_random:', list_random)
# e
list_50: list[int] = [number for number in list_random if number > 50]
print('list_50:', list_50)
# f
list_f: list[int] = [random.randint(1, 100) for i in range(10) if i > 50]
print('list_f:', list_f)

# g
sentence: str = input('give me a sentence?')
list_spaces: list[str] = [letter for letter in sentence if letter != ' ' and letter != 't']
print('list_spaces:', list_spaces)

# h
list_10_99: list[int] = [random.randint(10, 99) for i in range(10)]
print('list_10_99:', list_10_99)
new_list_99_10: list[int] = [i % 10 for i in list_10_99]
print('new_list_99_10:', new_list_99_10)
# end
