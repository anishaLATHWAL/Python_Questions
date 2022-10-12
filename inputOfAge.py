# take input of age from three peoples determine the oldest. 

one = int(input("Enter the first age: "))
second = int(input("Enter the second age: "))
third = int(input("Enter the third age: "))

if one > second and one > third :
    print("one is oldest ")

elif second > third and second > one:
    print("second is oldest ")

elif third > one and third > second:
    print("third id oldest ")

else: 
    print("all the three ages are same.")
