def calcPowerSum(power):
	sum = 0
	digits = []
	originalPowerString = str(2**power)
	for i in originalPowerString:
		digits.append(i)
	for i in digits:
		sum += int(i)
	print sum	

calcPowerSum(1000)