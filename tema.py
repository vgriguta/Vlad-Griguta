from typing import List

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

my_list = sorted(my_list, reverse=True)

print(my_list)

my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

my_list = sorted(my_list, reverse=False)

print(my_list)

my_sliced_list = my_list[4:]

print(my_sliced_list)

only_odd = [num for num in my_list if num % 2 == 1]

print(only_odd)







