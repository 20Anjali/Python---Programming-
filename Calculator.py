val_1 = int(input("Enter first value: "))
val_2 = int(input("\nEnter second value: "))
Operator = input("\nenter operator (+,-,*,/,%): ")

if Operator == "+" :
    print(val_1 + val_2)
if Operator == "-" :
    print(val_1 - val_2)
if Operator == "*" :
    print(val_1 * val_2)
if Operator == "/" :
    print(val_1 / val_2)
if Operator == "%" :
    print(val_1 % val_2)                
else:
    print("Invalid operator.")