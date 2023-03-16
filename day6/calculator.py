condition_to_run = True
symbols = "+ , - , * , /"

last_result = []
result_operation = 0

#this is a test git
def soma(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divided(a, b):
    return a / b


def minus(a, b):
    return a - b


while condition_to_run:
    operation = input(f"Please type the operation do you want  {symbols}\n")
    value1 = float(input("Type the first value"))
    value2 = float(input("Type the second value"))

    if operation == "+":

        result_operation = soma(value1, value2)
        print(result_operation)
    elif operation == "-":

        result_operation = minus(value1, value2)
        print(result_operation)
    elif operation == "*":
        result_operation = multiply(value1, value2)
        print(result_operation)
    elif operation == "/":

        result_operation = divided(value1, value2)
        print(result_operation)
    continue_calculus = input("Do you want continue calculing,using the last operation? Type Yes or No")

    if continue_calculus.lower() == "yes":
        condition_to_run = True
        last_result.append(result_operation)
        # last_result = result_operation

    elif continue_calculus.lower() == "no":
        condition_to_run = False
        for operation in last_result:
            result_operation = last_result + result_operation
        print(f"The result of operation plus the last result is equal to {result_operation}")

for operation in last_result:
    print(operation)
    print(last_result[operation])
