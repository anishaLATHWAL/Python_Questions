# a company decided to give bonus of 1000 rs to employee if his/her service is more than 5 years
# ask user their salary and year of service and print the net bonus amount.

x = int(input("What is current salary: "))
y = int(input("What is year of services: "))

if y > 5:
    print("You received a bonus of Rs 1000 and your current salary is", x+1000)

else :
    print("You did not receice bonus and your salary is",x)