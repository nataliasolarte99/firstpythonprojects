import random

question = input("Question: ")
random_number = random.randint (1,9)

if random_number == 1:
    print("Definitely yes")

elif random_number ==2:
    print("Yes")
elif random_number ==3:
    print("Maybe yes")
elif random_number ==4:
    print("Not clear")
elif random_number ==5:
    print("Maybe")
else:
    print("No")