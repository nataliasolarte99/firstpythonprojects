#If

age = int(input("Enter your age:"))

if age >= 18:
    print("You are now signed up!")

elif age < 0:
    print("You haven't been born yet")

elif age >= 100:
    print("You are too old to sign up")

else:
    print("You must be 18+ to sign up")