# User details

print("Hi, what is your name and age?")
name = input()
age = int(input())
print(f"Hi {name.capitalize()} , I am a bit older, I am {age * 2} years old.")
print (" What is your address?")
street = input()
house_number = input()
print(f" Wow you live at {street} {house_number}? My street name is similar, its {name[-4:]}!")

# dob = input()
# print(dob + ":Wow we are born in the same year!")