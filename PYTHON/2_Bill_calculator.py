print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $\n"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? \n"))
number_people = int(input("How many people to split the bill? \n"))

percentage_give = (total_bill * percentage_tip) / 100
total_amount = total_bill + percentage_give
amount_to_pay = round((total_amount / number_people), 2)


print(f"Each person should pay: ${amount_to_pay}")
