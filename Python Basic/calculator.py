import calculator_art 
def add(n1,n2):
    """ Add two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Subtrct Two number"""
    return n1 - n2

def multiply (n1, n2):
    """ Multiply two number"""
    return (n1 * n2)

def divide (n1, n2):
    """ Divide Two number"""
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# calculator_is_on = True

# while calculator_is_on is True:
#     num1 = int(input("What's the first number: "))
#     for symbol in operations:
#         print(symbol)
#     operation_symbol = input("Pick an operation : ")
    
#     num2 = int(input("What's the next number:"))
    
#     calculatio_function =  operations[operation_symbol]
#     first_answer = calculatio_function (num1, num2)

#     print(f'{num1} {operation_symbol} {num2} = {first_answer}')  
#     user_input = input(f'Type "y" to continue with {first_answer} or type "n" to exit.: ')

#     continue_calculation = True
    
#     while continue_calculation is True:

#         if user_input == "y":
#             # for symbol in operations:
#             #     print(symbol)
#             operation_symbol = input("Pick an operation from the lines above: ")
#             calculatio_function =  operations[operation_symbol]
#             num = int(input("Enter the next number :"))
            
#             answer = calculatio_function (first_answer, num)
#             first_answer = answer
            
#             print(answer)
#             user_input = input(f'Type "y" to continue with {first_answer} or type "n" to exit.: ')
 
#         else:
#             continue_calculation = False
#             calculator_is_on = False  
      

                

def calculator():  
    print(calculator_art.logo)
    
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol= input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f'{num1} {operation_symbol} {num2} = {answer} ')

        if input(f'Type "y" to continue with {answer} or type "n" to start a new calculator:  ') == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()