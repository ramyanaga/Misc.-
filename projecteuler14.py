#project euler 14? 
#pseudeocode: 

maxLength = 0
for i in range(1,50):
	#startNumb = i
	chainNumb = i
	chainValues = [] #the actual chain
	allChains = [] #list with lists of all chains
	chainLengths = [] #holds lengths of chains 
	#maxLengthIndex = 0
	while (chainNumb > 1):
	#for i in range(1,10):
		if chainNumb % 2 == 0:
			chainNumb = chainNumb/2
		else:
			chainNumb = (3*chainNumb) + 1
		chainValues.append(chainNumb)
	allChains.append(chainValues)
	print allChains
	#print allChains
	print allChains
#for i in allChains: 
	#print i 

"""
for element in allChains:
	chainLengths.append(len(element))
	print chainLengths
for element in chainLengths: 
	if element > maxLength:
		print maxLength
		print element
		maxLength = element
			#maxLengthIndex = chainLengths.index(maxLength)
			#print maxLengthIndex		
"""



