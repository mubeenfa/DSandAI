age = int(input("Enter your age: "))

if age < 10:
    if age ==0:
        print("Infant")
    elif age >=1 and age <12:
        print("Child")
elif age >=12 and age < 20:
    print("Teenager")
elif age >= 20 and age < 45:
    print("Adult")
else:
    print("Senior")