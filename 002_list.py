# LIST
# [], Index, ordered, duplicates allowed, mutable


my_list = [1, 3, 2, 6, 8, 8]

# access first element
print(my_list[0])

# second element
print(my_list[1])

# first three letter
print(my_list[0:3])

# access first and third element
print(my_list[0:3:2])

# access last letter
print(my_list[-1])

# reverse
print(my_list[::-1])
reversed_string = my_list.reverse()
# print(my_list.reverse())
print(reversed_string)
print(my_list)
my_list.reverse()
print(my_list)

my_list[0] = 1000
print(my_list)
