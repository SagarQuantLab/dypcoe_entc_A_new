class maths:

    def __init__(self, first_num, second_num):
        self.first_num = first_num
        self.second_num = second_num

    def addition(self):
        return self.first_num + self.second_num
    
class additionOperation(maths):

    def __init__(self, first_num, second_num):
        maths.__init__(self, first_num, second_num)

    def addition(self):
        return self.first_num * self.second_num

# mathsIns = maths(2, 3)
# print(mathsIns.addition())

additionOperationIns = additionOperation(2, 3)
print(additionOperationIns.addition())
