####### NORMAL SYNTAX

# for iterator in iterableObject:
#     pass

for i in range(4):
    print(i)

for i in range(0, 4):
    print(i)

for i in range(0, 4, 1):
    print(i)

my_list = [1, 3, 2, 6, 8, 8]

# element called via index
for i in range(len(my_list)):
    print(i, my_list[i])

# element called using 
i = 0
for each_elemet in my_list:
    if i == 3:
        print(each_elemet)
    i += 1

# enumerate
for i, val in enumerate(my_list):
    print(i, val)

#for loop in dictionary

my_dict = {
    "Name":"Rohan",
    "Age": 35,
    "Gender":"Male"
}

for each_key in my_dict.keys():
    print(my_dict[each_key])