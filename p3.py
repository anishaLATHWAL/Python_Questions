def calculator(num1,num2,op):
    if op == '+':
        return num1+num2

    elif op == '-':
        return num1 - num2
    elif op == '*':
       return num1 *num2
    elif op == '/':
        return num1/ num2
    else:
        print("Cannot perform th calculations..")
num1= float(input("Enter num1: "))
num2= float(input("Enter num2: "))
op= input("Enter the operator:")
ans= calculator(num1,num2,op)
print(ans)