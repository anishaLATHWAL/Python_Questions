a= float(input("Enter the lenght 1 of the triangle:"))
b= float(input("Enter the lenght 2 of the triangle:"))
c= float(input("Enter the lenght 3 of the triangle:"))
s= a+b+c/2
area = (s*((s-a)*(s-b)*(s-c)))**0.5
print("The area of the triangle using the heron's formula is",area)
