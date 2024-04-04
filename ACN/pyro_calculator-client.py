import Pyro4

ns = Pyro4.locateNS()
uri = ns.lookup("calculator")  # Change "myserver" to "calculator"

calculator = Pyro4.Proxy(uri)

operation = input("Enter operation (add, subtract, multiply, divide): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if operation == "add":
    result = calculator.add(a, b)
elif operation == "subtract":
    result = calculator.subtract(a, b)
elif operation == "multiply":
    result = calculator.multiply(a, b)
elif operation == "divide":
    result = calculator.divide(a, b)
else:
    print("Invalid operation")
    exit()

print("Result:", result)