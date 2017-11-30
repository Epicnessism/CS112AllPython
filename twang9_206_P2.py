#-------------------------------------------------------------------------------
# Name: Tony Wang
# G#: G00969838
# Project 2
# Lab Section 206
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: python documentation, exercises 1,2.
#-------------------------------------------------------------------------------
# Comments and assumptions:
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <= 80 characters to facilitate printing.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------
#rounding function, calculates the coefficient of shipping, compute cost
def rounding():
	#finding the remainder of the distance
	distance_remainder = distance_ship % 200
	#check if completely divided or if rounding is needed
	if distance_remainder > 0:
		#finding distance coefficient, no remainder
		distance_coef = distance_ship//200
		#adding 1 to the coefficient to compensate for remainder
		distance_coef += 1
		#multiplying distance coefficient to shipping rate
		ship_cost = distance_coef * rate_ship
		#converting ship_cost to a float variable
		ship_cost = float(ship_cost)
		#check to make sure the shipping cost is greater than 1 penny
		if ship_cost <= 0.01:
			#if it is not, set it equal to 1 penny
			ship_cost == 0.01
		#printing the ship cost to the user
		print("\nShipment charge: $%.1f" % ship_cost)
	#if the remainder is 0, that means it doesnt need rounding
	elif distance_remainder == 0:
		#simpling floor division to find coefficient to multiply by
		distance_coef = distance_ship//200
		#multiply distance coefficient by shipping rate
		ship_cost = distance_coef * rate_ship
		#convert ship_cost to a float variable
		ship_cost = float(ship_cost)
		#check if shipping cost is less than 1 penny
		if ship_cost <= 0.01:
			#sets shipping cost to 1 penny
			ship_cost == 0.01
		#print the ship cost to the user
		print("\nShipment charge: $%.1f" % ship_cost)

	return


#asking user for weight
weight_ship = float(input("Weight of shipment(lbs): "))

#checking weight if over 50
if weight_ship > 50:
	#notifies user if too heavy
	print('\nToo heavy!')
#when weight is less than or equal to 50
elif weight_ship <= 50 and weight_ship > 0:
	#ask user if they want express shipping
	express_ship = input("Express shipment? ")
	#checks to see if answer is no
	if express_ship == 'no' or express_ship == 'n':
		#checks if weight is less than 0.01
		#if it were less than this
		#ship cost would be less than 1 penny
		if weight_ship <= 0.01:
			#if so, sets ship cost to 1 penny
			ship_cost = 0.01
			#prints shipping cost
			print("\nShipment charge: $%.2f" % ship_cost)
		#when weight is greater than 0.01
		elif weight_ship > 0.01:
			#multiply weight by .5
			ship_cost = weight_ship * .5
			#prints ship cost to user
			print("\nShipment charge: $%.1f" % ship_cost)
	#checks to see if answer is yes
	elif express_ship == 'yes' or express_ship == 'y':
		#ask for shipping distance
		distance_ship = float(input("Distance of shipment(miles): "))
		#checks to see if distance is greater than 12450
		if distance_ship > 12450:
			#notifies user distance is too great
			print("\nOut of range of Earth's surface!")
		#otherwise distance less than 12450
		elif distance_ship <= 12450:
			#weight less than 3
			if weight_ship <= 3:
				#defines shipment rate
				rate_ship = 3
				#calls rounding function
				rounding()
			#weight greater than 3, less than 10
			elif weight_ship > 3 and weight_ship <= 10:
				#defines shipment rate
				rate_ship = 6.5
				#calls rounding function
				rounding()
			#weight greater than 10, less than 20
			elif weight_ship > 10 and weight_ship <= 20:
				#defines shipment rate
				rate_ship = 14
				#calls rounding function
				rounding()
			#weight greater than 20
			elif weight_ship > 20:
				#defines shipment rate
				rate_ship = 30
				#calls rounding function
				rounding()


