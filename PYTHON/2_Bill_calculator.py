print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
percentage_tip = int(input("what percentage tip would you like to give?")) / 100
total_people = int(input("How many people to split the bill?"))

total_tip = total_bill * percentage_tip
amount_to_pay = round((total_tip + total_bill) / total_people, 2)

print(f" Each person should pay: {amount_to_pay}")