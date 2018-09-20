# Flint Eller
# 9/21/18
# This is a chat bot that chats about, names, places, favorite, numbers, amd cars.

print("Hello there!")

user_name = input("What is your name?")

print("Well hey there", user_name, "I'm Pixel, a chat bot created by Flint")

user_place = input("Where are you from?")

print("Cool,", user_place, "sounds like a great place!")

pixel_fav_number = 10.0

user_fav_number = float(input("What is your favorite number?"))

# This checks if the user entered the same favorite number as Pixel,
# then prints a different message based on what the number is
if pixel_fav_number == user_fav_number:
    print("Woah, ten is my favorite number too!")

elif pixel_fav_number != user_fav_number:
    neg_fav_number = pixel_fav_number - user_fav_number
    print("Cool, your favorite number (", user_fav_number, ") is ", abs(neg_fav_number),
          "away from my favorite number (10).")

else:
    print("Please enter a number")

user_car = input("What is your dream car?")

print("Awesome, the", user_car, "is a great car!")

car_cost = int(input("How much would a car like that cost?"))

print("Wow that's a lot.")

annual_interest = float(input("What would be a reasonable annual interest rate for a car such that?"))

loan_years = float(input("How many years would you take a loan out for?"))

monthly_rate = annual_interest / 100 / 12

number_payments = loan_years * 12

# This calculates the monthly payments
month_payment = (monthly_rate * car_cost)/(1 - (1 + monthly_rate) ** -number_payments)

total_cost = month_payment * number_payments

print("If you were to buy the", user_car, "for", car_cost, ", you would pay", month_payment,
      "every month, and a total cost of", total_cost)

print("I really enjoyed chatting with you", user_name, "gotta go, bye!")
