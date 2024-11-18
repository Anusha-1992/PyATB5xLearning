# Program - if age > 18 - allowed to vote
# else -> not allowed too

user_age = int(input("Enter the age "))

if user_age >18:
    print(" you are eligible for vote")
else:
    print(" not eligible for vote")

print("---------*************----------")

# Ternary opertor

print("you are eligible for movie" if user_age >18 else "not eligible for movie")

print("---------*************----------")

print("you are eligible for PUB"if int(input("Enter into the Pub")) > 18 else "not eligible for PUB")