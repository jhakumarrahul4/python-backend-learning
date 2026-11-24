#Generate a list of squares of numbers from 1 to 20.
numbers=[num for num in range(1,21)]
print(numbers)
squares=[num*num for num in numbers]
print(squares)

#Given a list of employee salaries, create a new list containing salaries greater than 30,000.

salaries=[25000, 35000, 45000, 55000, 65000]
new_list=[salary for salary in salaries if salary > 30000]
print(new_list)

#Given a list of employee names, create a dictionary where each name is mapped to its character count.

employees=["Rahul", "Priya", "Amit", "Sneha"]
dictionary={name:len(name) for name in employees}
print(dictionary)