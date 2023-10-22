from functions import addition, subtraction, multiplication, division
from operations import get_numbers, get_operator, continue_calculations

def calculator(a, b, action):
    if action == "+":
        return addition(a, b)
    elif action == "-":
        return subtraction(a, b)
    elif action == "*":
        return multiplication(a, b)
    elif action == "/":
        return division(a, b)
    else:
        print("Invalid operator.")
        
def main():
    while True:
        a, b = get_numbers()       
        action = get_operator()
        result = calculator(a, b, action)
        print(f"Result is {result}")

        if not continue_calculations():
            break

if __name__ == "__main__":
    main()
