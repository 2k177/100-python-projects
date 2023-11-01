def add(a, b):
  return a+b

def subtract(a, b):
  return a-b

def multiply(a, b):
  return a*b

def divide(a, b):
  return a/b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

for op, func in operations.items():
  print(f" Operation : {op}")

exit_flag = False
while not exit_flag:
  operator = input("Pick any operation ")
  if operator in operations:
    result = operations[operator](num1, num2)
    print(f"The result of {num1} {operator} {num2} = {operations[operator](num1, num2)}")
  else:
    print("Invalid operator")
  continue_flag = input("Type Y to continue with the previous result or N to exit")
  if continue_flag.lower() == "y":
    num1 = result
    num2 = int(input("Enter the second number"))
  else:
    exit_flag = True
    
