import math

def calFuel(mass):
	return math.floor(mass / 3) - 2

if __name__ == '__main__':

	file_name = 'input.txt'

	f = open(file_name, 'r')

	fuel_total = 0

	for line in f:
		fuel = calFuel(float(line))
		fuel_total += fuel
		ex_fuel = calFuel(fuel)

		while ex_fuel > 0:
			fuel_total += ex_fuel
			ex_fuel = calFuel(ex_fuel)

	print fuel_total