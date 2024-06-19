def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  if num2 == 0:
    return "Error: Cannot divide by zero."
  else:
    return num1 / num2

while True:
  print("Enter operation (+, -, *, /): ")
  operator = input()

  print("Enter first number: ")
  num1 = float(input())
  print("Enter second number: ")
  num2 = float(input())

  result = None
  if operator == "+":
    result = add(num1, num2)
  elif operator == "-":
    result = subtract(num1, num2)
  elif operator == "*":
    result = multiply(num1, num2)
  elif operator == "/":
    result = divide(num1, num2)
  else:
    print("Invalid operator.")

  if result is not None:
    print("Result: ", result)

  print("Do you want to continue? (y/n): ")
  choice = input()
  if choice.lower() != "y":
    break

