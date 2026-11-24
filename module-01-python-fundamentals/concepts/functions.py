def greet():
    print("Welcome to python backend development")

greet()

def greet_employees(name): #name is parameter
    print(f"Welcome {name}")

greet_employees("Rahul") #Rahul is argument

def calculate_salary(basic_salary,bonus):
    total_salary=basic_salary+bonus
    return total_salary

print("Total salary :",calculate_salary(10000,2000))

def create_employees(name,department="IT"):
    print(f"Hello {name}, you are working in {department} department")

create_employees("Rahul")
create_employees("Amit","HR")
create_employees(department="Sales",name="Pranav") 
