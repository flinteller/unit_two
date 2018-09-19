# Flint Eller
# 9/21/18
# This is a chatbot that chats about, names, places, favorite, numbers, amd cars.

print("Hello there!")

user_name = input("What is your name?")

print("Well hey there", user_name , "I'm Pixel, a chatbot created by Flint")

user_place = input("Where are you from?")

print("Cool,", user_place, "sounds like a great place!")

pixel_fav_number = 10.0

user_fav_number = float(input("What is your favorite number?"))

if pixel_fav_number == user_fav_number:
   print("Woah, ten is my favorite number too!")


elif pixel_fav_number != user_fav_number:
    neg_fav_number = pixel_fav_number - user_fav_number
    print("Cool, your favorite number (", user_fav_number, ") is ", abs(neg_fav_number), "away from my favorite number (10).")

else:
   print("Please enter a number")

user_car = input("What is your dream car?")

print("Awesome, the", user_car, "is a great car!")

car_cost = input("How much would a car like that cost?")

print("Wow that's a lot.")

annual_interest = input("What would be a reasonable annual interest rate for a car such that?")

loan_years = int(input("If you were to get a loan for the car, for how many years would you like to take that loan out?"))

monthly_rate = annual_interest / 100 / 12

number_payments = loan_years * 12

month_payment = (monthly_rate * car_cost)/(1 - (1 + monthly_rate)** -number_payments)





