import calculator_art

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
    print(calculator_art.logo)
    num1 = float(input("What is the first number?: "))

    for operation in operations:
        print(operation)


    is_playing = True
    while is_playing:
        selected_operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        operation_function = operations[selected_operation]

        answer = operation_function(num1, num2)

        print(f"{num1} {selected_operation} {num2} = {answer}")

        question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")
        if question == "y":
            num1 = answer
            is_playing = True
        elif question == "n":
            is_playing = False
            calculator()

calculator()




