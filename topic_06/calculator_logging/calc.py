from functions import addition, subtraction, multiplication, division
from operations import get_numbers, get_operator, continue_calculations
import os

current_directory = os.getcwd()
path_to_logs = os.path.join(current_directory, 'topic_06', 'calculator_logging', 'calc.log')

try:
    file = open(path_to_logs, 'a')
except IOError as e:
    print(e)

def calculator(a, b, action):
    try:
        if action == "+":
            return addition(a, b)
        elif action == "-":
            return subtraction(a, b)
        elif action == "*":
            return multiplication(a, b)
        elif action == "/":
            return division(a, b)
        else:
            error_message = "Invalid operator: " + action + "."
            print(error_message + '\n')
            file.write(error_message + '\n')
    except ZeroDivisionError:  
        print("Division by 0 is forbidden.")
        file.write('User tried to divide by zero.\n')
        
def main():
    while True:
        a, b = get_numbers()
        if a is None or b is None:
            file.write('User entered wrong value when entering numbers.\n')
            continue
        action = get_operator()
        result = calculator(a, b, action)
        if result is not None:
            print(f"Result is {result}")
            log_message = f'User entered numbers {a} and {b}, action "{action}", received the result: {result}.'
            file.write(log_message + '\n')
        if not continue_calculations():
            break

if __name__ == "__main__":
    main()
    file.close()
