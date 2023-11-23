# Tip calculator
bill_total = float(input("What is your bill? "))
total_tip = int(input("How much tip would you like to give? "))
people = int(input("How many pepople to split the bill? "))
bill = round(bill_total / people, 2)
tip = round(bill_total / 100 * total_tip / people, 2)
print(f"You should pay {bill}$ for the bill and give {tip}$ tips, {bill + tip}$ in total")