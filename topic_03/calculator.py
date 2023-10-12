def calculator(a, b, action):
    if action == "+":
        result = a + b
        return result
    elif action == "-":
        result = a - b
        return result
    elif action == "*":
        result = a * b
        return result
    elif action == "/":
        if b == 0:
            print ("Division by 0 is forbidden.")
            return
        else:
            result = a / b
            return result
        
def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    action = (input("Enter ation (+, -, * or /): "))

    print("Result is " + str(calculator(a, b, action)))

while True:
    trigger = input("Do you want to continue?[Y/N]").upper()
    if trigger == "N":
        break
    elif trigger == "Y": 
        main()
    else:
        print("Try again!")
    