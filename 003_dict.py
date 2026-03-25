# DICT
# {}, ordered, no duplicates allowed, mutable, key

my_dict = {
    "Name":"Rohan",
    "Age": 35,
    "Gender":"Male",
    "Name": "Sohan"
}
print(my_dict)

# access value of name
print(my_dict["Name"])

# access all keys
print(my_dict.keys())

# access all values
print(my_dict.values())

# access key and value
print(my_dict.items())

#################################################################
# ITEMS     SYMBOLS      CALLING      MUTABLE      DUPLICATE    ORDERED
# LIST         []           Index       Y              Y            Y
# DICT         {}           Keys        Y              N            Y
# TUPLE        ()           Index       N              Y            Y
# SETS         {}           -           N              N            N
