# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter second number: "))

# Request user input operator
operator = input("Select an operator (+, -, *, /): ")

# Calculate the result
if operator == "+":
     result = num1 + num2
elif operator == "-":
     result = num1 - num2
elif operator == "*":
     result = num1 * num2
elif operator == "/":
     result = num1 / num2
else:
     print("Incorrect statement")

# Display the result on the screen
print("Result: ", result)
