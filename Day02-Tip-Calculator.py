print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
tip_percent = tip/100
tip_amount = bill * tip_percent
bill_with_tip = bill + tip_amount
bill_per_person = round(bill_with_tip/people,2)
print(f"Each person should pay: ${bill_per_person}")


