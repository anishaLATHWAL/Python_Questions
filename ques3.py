'''create a function using the following conditions
It should acept employee name and salary and display both
if the salary is missing in the function and assign default value to the salary
Ben(9000),mike(15000),bob()  '''

def sal(name,salary=5000):
    print(name,salary)
sal("Ben",9000)
sal("mike",15000)
sal("bob")


