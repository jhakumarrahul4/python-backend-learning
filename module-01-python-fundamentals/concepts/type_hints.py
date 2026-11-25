#Create a function accepting two integers and returning their sum. Add appropriate type hints.
def add(a:int,b:int)-> int:
    return a+b

print(add(10,20))

#Create a function that accepts a list of integers and returns their average.
def calculate_average(l:list[int])->float:
    return sum(l)/len(l)

print(calculate_average([10,20,30,40,50]))

#Create a function that accepts an employee ID and returns an employee name or None if the employee doesn't exist.

def get_employee_name(employee_id:int)->str|None:
    employee_database={1:"John Doe",2:"Jane Smith",3:"Alice Johnson"}
    return employee_database.get(employee_id)

print(get_employee_name(1))
print(get_employee_name(4))
