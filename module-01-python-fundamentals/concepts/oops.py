#classes and Objects
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def display(self):
        print(f"Employee name is {self.name} and salary is {self.salary}")

emp1=Employee("Rahul",10000)
emp2=Employee("Amit",20000)
emp1.display()
emp2.display()

#Inheritence
class Developer(Employee):
    def display(self):
        print(f"Developer name is {self.name} and salary is {self.salary}")

class Manager(Employee):
    def display(self):
        print(f"{self.name} is managing team and salary is {self.salary}")


dev1=Developer("Pranav",30000)
dev1.display()
manager1=Manager("Rohit",40000)
manager1.display()

#Composition
class Department:
    def __init__(self,department_name):
        self.department_name=department_name
        self.employees=[]

    def add_employees(self,employee):
        self.employees.append(employee)

    def display_employees(self):
        print(f"Employees in {self.department_name} department:")
        for emp in self.employees:
            emp.display()

it_department=Department("IT")
it_department.add_employees(emp1)
it_department.add_employees(emp2)
it_department.display_employees()





    

        