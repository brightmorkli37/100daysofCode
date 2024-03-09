print("Welcome to the tip calculator")

bill = float(input("What was the total bill: "))

tip_percent = int(input("What percentage tip would you like to give? (10, 12, 15) "))

number_of_people = int(input("How many people to split the bill? "))

amount_payable = ((tip_percent / 100) * bill) + bill

bill_per_person = round(amount_payable / number_of_people, 2)

print(f"Each person should pay ${bill_per_person}")
