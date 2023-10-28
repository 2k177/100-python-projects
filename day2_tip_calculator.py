#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator.\n")
total_bill = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_ppl = int(input("How many people to split the bill? "))
#Each person should pay (150.00 / 5) * 1.12 = 33.6
total_bill = total_bill * (1+tip/100)
indvidual_bill = total_bill / num_of_ppl
#Format the result to 2 decimal places = 33.60
final_bill = round(indvidual_bill, 2)
print(f"\nEach person should pay: ${final_bill}")
