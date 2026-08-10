""" Evaluate the change given back to the customer and determine
to give back in coins and notes, using only arithmetic ops."""

total_cost = float(input('Total cost: '))

while True:
	customer_payment = float(input('Payment: '))
	change = customer_payment - total_cost	

	if change > 0:

		cents = change % 1
		dollars = change - cents

		quarters = cents // .25
		cents = round(cents % .25, 2)

		dimes = cents // 0.10
		cents = round(cents % .10, 2)

		nickels = cents // .05
		cents = round(cents % .05, 2)

		pennies = cents // 0.01

		print('Dollars: ' + str(int(dollars)))
		print('Quarters: ' + str(int(quarters)))
		print('Dimes: ' + str(int(dimes)))
		print('Nickels: ' + str(int(nickels)))
		print('Pennies: ' + str(int(pennies)))

		break
	else:
		print('You didn\'t provide enough money. Reassess and pay.')
