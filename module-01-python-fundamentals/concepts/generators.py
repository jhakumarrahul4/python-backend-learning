#Iterators
employees = ["Rahul", "Priya", "Amit", "Sneha"]
iterator = iter(employees)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))  This will raise StopIteration error since there are only 4 employees

#Generators
def generate_numbers():
    for i in range(1,11):
        yield i

for num in generate_numbers():
    print(num)

#Create a generator that reads a list of employee names and returns one employee at a time.
def generate_employees(employees):
    for employee in employees:
        yield employee

for employee in generate_employees(employees):
    print(employee)