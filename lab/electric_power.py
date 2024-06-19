# An electric power distribution company charges domestic customers as
# follows: Consumption unit Rate of charge:
#   1.2.1. 0-200 Rs. 0.50 per unit
#   1.2.2. 201-400 Rs. 0.65 per unit in excess of 200
#   1.2.3. 401-600 Rs 0.80 per unit excess of 400
#   1.2.4. 601 and above Rs 1.00per unit excess of 600
#   1.2.5. If the bill exceeds Rs. 400, then a surcharge of 15% will be charged,
#          and the minimum bill should be Rs. 100/-
# Create a Python program based on the scenario mentioned above.

rate_charge = float(input("enter the amount of energy consumed : "))
amount = 0
if rate_charge <200 : amount = rate_charge * 0.50
if rate_charge in range(201,400) : amount = (200 * 0.50) + ((rate_charge - 200) * 0.65)
if rate_charge in range(401,600) : amount = (200 * 0.50) + (200 * 0.65) + ((rate_charge - 400) * 0.80)
if rate_charge > 601 : amount = (200 * 0.50) + (200 * 0.65) + (200 * 0.80) + ((rate_charge - 600) * 1.00)

bill = max(amount,100)
if bill > 400 :
    bill = bill + bill * 0.15
print("Electricity bill to be paid: ",amount)