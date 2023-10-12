def disk_calculation(a, b, c):
    D = b**2 - 4*a*c
    return D 

def calculation(a, b, D):
    print("D is " + str(disk_calculation(a, b, c)))
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        return x1, x2
    if D == 0:
        x1 = (-b + D**0.5) / (2*a)
        return x1
    if D < 0:
        return "Equation has no roots."

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(calculation(a, b, disk_calculation(a, b, c)))
