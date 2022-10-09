# Company will give bonus based on the follwing criteria.
# Time spent in company                   Bonus
#   greater than 10 years                 10%
#   more than 6 and less than 10          8%
#    less than 6                          5%
# ask the salary and time spent from the user
# print the net bonus amount accordingly

salary = int(input("Enter your current salary: "))
time = int(input("Enter the time spent in the company: "))

if time > 10 :
    print("now your salary is ", salary + salary*(10/100))

elif time > 6 and time < 10 :
    print("now your salary is ", salary + salary*(8/100))

elif time < 6 :
    print("now your salary is ", salary + salary*(5/100))

else:
    print("you did not receive any bonus")