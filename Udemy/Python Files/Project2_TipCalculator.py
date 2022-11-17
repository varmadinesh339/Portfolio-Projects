# This is the Tip Calculator Program
print("Welcome to the tip calculator program")

total_Bill = float(input("What was the total_Bill ? "))

split_Bill = int(input("How many people to split the bill ? "))

tip_perc = int(input("What percentage tip would you like to give 10, 12 or 15 ? "))

per_Person = (total_Bill*(1+(tip_perc/100)))/split_Bill

print(f"Each person should pay : {round(per_Person,2)}")