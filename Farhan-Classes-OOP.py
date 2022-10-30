# =======================Class with methods======================
'''class Employee:
    
    def __init__(self, first_name, last_name, salary, middle_name=''):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary

    def __str__(self):

        if self.middle_name != "":
            return f'First Name: {self.first_name}\nMiddle Name: {self.middle_name}\nLast Name: {self.last_name}\nSalary: {self.salary}'
        else:
            return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nSalary: {self.salary}'


emp1 = Employee('Muhammad', 'Taimoor', 100000, 'Salahuddin')
emp2 = Employee('Azam', 'Shaheed', 120000)
print(emp1)
print()
print(emp2)'''

# =======================Class with class variables======================


import math


class Employee:
    number_of_employees = 0
    salary_increment = 1.10

    def __init__(self, first_name, last_name, salary, middle_name=''):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.salary = salary

        Employee.number_of_employees += 1

    def __str__(self):
        return f'{self.first_name} | {self.last_name} | {self.salary} | {self.middle_name}'
    # def __str__(self):
        '''if self.middle_name != "":
            return f'First Name: {self.first_name}\nMiddle Name: {self.middle_name}\nLast Name: {self.last_name}\nSalary: {self.salary}\nAnnual Salary Increment: {math.floor((self.salary_increment*100)-100)}%\nIncreased Salary: {math.floor(self.salary*self.salary_increment)}'
        else:
            return f'First Name: {self.first_name}\nLast Name: {self.last_name}\nSalary: {self.salary}\nAnnual Salary Increment: {math.floor((self.salary_increment*100)-100)}%\nIncreased Salary: {math.floor(self.salary*self.salary_increment)}'''

    @classmethod
    def from_string(cls, emp_str):
        first_name, last_name, salary, middle_name = emp_str.split('-')
        return cls(first_name, last_name, salary, middle_name)


emp1 = Employee('Muhammad', 'Taimoor', 100000, 'Salahuddin')
emp2 = Employee('Azam', 'Shaheed', 120000)
'''print(emp1)
print()
print(emp2)
print()
print(f'Total Employees: {Employee.number_of_employees}')'''

emp3 = 'Yasir-Shami-1000000-Asool'
print(emp3)

emp_str1 = Employee.from_string(emp3)
print(emp_str1)
