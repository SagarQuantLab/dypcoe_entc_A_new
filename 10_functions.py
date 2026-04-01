####
# def function_name():
#     pass

def my_decorator(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise ValueError(f"Expected int in first positional input argument recieved : {args[0]}")
        if not isinstance(args[1], int):
            raise ValueError(f"Expected int in second positional input argument recieved : {args[1]}")
        
        # check for kwargs
        if len(kwargs) > 0:
            key_list = list(kwargs.keys())
            if not isinstance(kwargs[key_list[0]], int):
                raise ValueError(f"Expected int in third keyword input argument recieved : {kwargs[key_list[0]]}")
            if not isinstance(kwargs[key_list[1]], int):
                raise ValueError(f"Expected int in fourth keyword input argument recieved : {kwargs[key_list[1]]}")
        else:
            kwargs.setdefault("third_num", 0)
            kwargs.setdefault("fourth_num", 0)
            
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def addition(first_num, second_num, third_num, fourth_num):
    sum = first_num + second_num + third_num + fourth_num
    return sum

sum = addition(2, 3)
# sum = addition(2, '3')
sum = addition(2, 3, third_num=4, fourth_num=5)
# sum = addition(2, 3, third_num='c', fourth_num='d')
print(sum)