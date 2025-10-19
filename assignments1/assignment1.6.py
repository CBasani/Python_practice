x = int(input("Can you fill in a score from 1 to 100? "))

if x > 100 or x < 1:
    print("You need to fill in a number between 1 and 100!")
elif x >= 90:
    print("Your grade is: A")
elif x >= 80 and x < 90:
    print("Your grade is: B")
elif x >= 70 and x < 80:
    print("Your grade is: C")
elif x >= 60 and x < 70:
    print("Your grade is: D")
elif x >=70 and x < 80:
    print("ok")
else:
    print("Your grade is: F")
