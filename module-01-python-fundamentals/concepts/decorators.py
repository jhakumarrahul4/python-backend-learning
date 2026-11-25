# Decorators allow you to add extra functionalities to existing functions without modifying their structure.

def my_decorator(func):

    def wrapper():
        print("Runs Before the function is called.")
        func()
        print("Runs After the function is called.")
    return wrapper

@my_decorator
def greet():
    print("Hello World")

greet()  # This will print the messages before and after calling greet function.

#Create a decorator that calculates and prints the execution time of a function using Python's time module.

import time
def calculate_execution_time(func):
    def wrapper(*args,**kwargs):
        start_time=time.time()
        result=func(*args,**kwargs)
        end_time=time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@calculate_execution_time
def add(a,b):
    time.sleep(2)
    return a+b

print("Result:", add(10, 20))

