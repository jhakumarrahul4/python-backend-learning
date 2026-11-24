try:
    a=10
    b=0
    print(a/b)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#multiple exceptions
try:
    number=int(input("Enter a number:"))
    result=10/number
    print(f"Result is {result}")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

finally:
    print("Program finished execution.")

#file handling exceptions
try:
    filename=input("Enter the filename :")
    file=open(filename,"r")
    content=file.read()
    print(content)

    file.close()
except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")

#custom exceptions
class InvalidAgeError(Exception):
    pass

age=int(input("Enter your age:"))

try:
    if age<0:
        raise InvalidAgeError("Age cannot be negative.")
    elif age<18:
        print("You are a minor.")
    else:
        print("You are an adult.")
except InvalidAgeError as e:
    print(f"Error: {e}")