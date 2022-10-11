from replit import clear
from art import logo


def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+":add, 
    "-": substract, 
    "*":multiply, 
    "/": divide
}
def calculation():
    print(logo)
    calculator_status = True
    num_1 = float(input("What's the first number?"))
    while calculator_status == True:
        num_2 = float(input("What's the next number?")) 
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation symbol above: ")
        #use keys() to call the dictionary when trying to find a key in the dictionary
        if operation_symbol not in operations.keys():
            print("You have input an invalid symbol.")
            return 
        function = operations[operation_symbol]
        answer = function(num_1, num_2)
        print(f"{num_1} {operation_symbol} {num_2} = {answer}.")
        
      
        if input(f"Type 'y' if you want to continue calculating using {answer} or 'n' to start a new calculation.") == "y":
            num_1 = answer
        else:
            calculating_status = False
            clear()
            calculation()
       
calculation()
