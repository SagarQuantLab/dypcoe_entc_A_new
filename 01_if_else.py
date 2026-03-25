# if else condition

my_age = 19

# if block
if my_age > 18:
    print("Adult")

# if else block
if my_age > 18:
    print("Adult")
else:
    print("Minor")

# if elif else block
if my_age > 18:
    print("Adult")
elif my_age == 18:
    print("Turing Minor")
else:
    print("Minor")

# reduce code
my_age = 18
msg = "Bye"
if isinstance(my_age, int):
    msg = "hello"

print(msg)