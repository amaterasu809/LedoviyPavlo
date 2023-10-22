def get_numbers():
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        return a, b
    except ValueError:
        print("Wrong input!")
       
def get_operator():
    return input("Enter action (+, -, * or /): ")

def continue_calculations():
    trigger = input("Do you want to continue? [Y/N]").upper()
    return trigger == "Y"
