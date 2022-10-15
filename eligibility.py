totalWORKINGdays = int(input("Total number of working days: "))
attended = int(input("Attended lectures are: "))
percentage = (attended/totalWORKINGdays)*100
if percentage > 75:
    print("You are eligible for exam")

else:
    print("You are not eligible for exam")
    