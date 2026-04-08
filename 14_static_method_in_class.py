class A:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def _get_my_private_details(self):
        return "You can access my private details - A"
    
    def __get_my_personal_details(self):
        return "You can't access my personal details - A"
    
    @staticmethod
    def get_addhar_number(name, age, gender):
        return f"Adhar number for person {name, age, gender} is - 1234 5678 9111"


class student(A):

    def __init__(self, name, age, gender):
        A.__init__(self, name, age, gender)


# studentIns = student('Rohan', 35, 'M')
# print(studentIns.name, studentIns.age, studentIns.gender)
# print(studentIns._get_my_private_details())
# # print(studentIns.__get_my_personal_details())
# print(student.get_addhar_number(studentIns.name, studentIns.age, studentIns.gender))


print(student.get_addhar_number('Rohan', 35, 'Male'))