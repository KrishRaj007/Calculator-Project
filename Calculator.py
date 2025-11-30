print("--- Calculator ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("+, -, *, /")
operator = input("Choose operator: ")

if operator == '+':
        print("Result:", a + b)
elif operator == '-':
        print("Result:", a - b)
elif operator == '*':
        print("Result:", a * b)
elif operator == '/':
        print("Result:", "Error" if b == 0 else a / b)
else:
        print("Invalid operator")