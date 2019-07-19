# OOPR-Exer-3
# Start writing your code here
class Employee:
    def __init__(self, name='None', age=None, salary=None):
        self.name = name
        self.age = age
        self.salary = salary


emp1 = Employee("Jack", 24, 30000)
emp2 = Employee("Jill", 27, 40000)

print(emp1.name, emp1.age, emp1.salary)

print(emp2.name, emp2.age, emp2.salary)

