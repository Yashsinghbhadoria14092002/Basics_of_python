class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        print(self.salary)

rohan = Employee("Rohan", "3455")
# print(rohan.salary)
# print(rohan.name)
rohan.getSalary()
harry = Employee("Harry", "345500000000")
# print(harry.salary)
# print(harry.name)
harry.getSalary()