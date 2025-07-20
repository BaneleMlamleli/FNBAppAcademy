import modules

def greet(name):
    print(f"Hello, {name}")

def add(num, num1):
    sum = num + num1
    print(sum)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def bulisa(name, greetings="hello"):
    print(f"{greetings}, {name}")

greet('James')
add(2,3)
print(factorial(5))
bulisa('Billy', 'Good day')
print(modules.add(2,3))