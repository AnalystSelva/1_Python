i = 10
if i == 10:
    print("Correct")

Password = input("Enter the password:")
if Password == "HOPE@123":
    print("Your password is correct")
else:
    print("Incorrect password")

Age = int(input("enter the age:"))
if Age <= 18:
    print("Children")
elif 18 < Age <= 25:
    print("Adult")
elif 25 < Age < 60:
    print("Citizen")
else:
    print("Senior Citizen")

number = int(input("Enter any number:"))
if number >= 0:
    print("positive Number")
else:
    print("negative number")

number = int(input("Enter a number to check:"))
try:
    if number % 5 == 0:
        print("No is divisible by 5")
    else:
        print("No is not divisible by 5")
except:
    print("error")
