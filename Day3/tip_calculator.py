print("############################################")
print("     Welcome to the tip calculator.")
print("############################################")

total_bill = float(input("What was the total bill?"))
percentage_tip = int(input("What percentage tip would you like to give? 10,12 or 15?"))
people_to_split = int(input("How many people to split the bill?"))

total_percentage = float(total_bill)* (percentage_tip/100)

total_to_pay =  round((total_bill + total_percentage)/people_to_split,2)
print(f"Each Person should pay: ${total_to_pay} ")