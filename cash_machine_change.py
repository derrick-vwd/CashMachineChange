""" Evaluate the change given back to the customer and determine
to give back in coins and notes, using only arithmetic ops."""

total_cost = float(input('Total cost: '))
customer_payment = float(input('Payment: '))

change = customer_payment - total_cost
# Assumes that the customer will pay the entire sum.

cents = round(change % 1, 2)
dollars = change - cents

quarters = cents // .25
cents = round(cents % .25, 2)

nickels = cents // .05
cents = round(cents % .05, 2)

dimes = cents // 0.10
cents = round(cents % .10, 2)

pennies = cents // 0.01

print('Dollars: ' + str(dollars))
print('Quarters: ' + str(quarters))
print('Nickels: ' + str(nickels))
print('Dimes: ' + str(dimes))
print('Pennies: ' + str(pennies))
