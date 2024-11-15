def CtoF(C):
    F = (C * 9 / 5) + 32
    return F
    
def FtoC(F):
    C = (F - 32) * 5/9
    return C

print("Choose a conversion:")
print("\t 1.Celsius to Fahrenheit \n\t 2.Fahrenheit to Celsius")

n = int(input("Enter an option:"))

if n == 1:
    c = float(input("Enter the temparature in celsius:"))
    print("The temparature in Fahrenheit is:" , CtoF(c))

if n == 2:
    f = float(input("Enter the temparature in fahrenheit:"))
    print("The temparature in Celsius is:" , FtoC(f))


