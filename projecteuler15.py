from datetime import datetime
def calcPowerSum(exponent):
	stringValList = []
	intValList = []
	sum = 0
	stringVal =  str(2**(exponent))
	for i in stringVal:
		stringValList.append(i)
		sum += int(i)
	"""print stringValList
	for i in stringValList:
		intValList.append(int(i))
	for i in intValList:
		sum+= i
	print intValList
	print sum
	"""
	print sum
if __name__ == "__main__":
	start = datetime.now()
	calcPowerSum(1000)
	end = datetime.now()
	print start - end 