def calculator(a, b, action):
    match action:
        case "+":
            result = a + b
            return result
        case "-":
            result = a - b
            return result
        case "*":
            result = a * b
            return result
        case "/":
            if b == 0:
                print ("Division by 0 is forbidden.")
                return
            else:
                result = a / b
                return result
        
def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    action = (input("Enter ation (+, -, * or /)"))

    print("Result is " + str(calculator(a, b, action)))

main()