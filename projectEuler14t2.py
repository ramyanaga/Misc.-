allFullChains = []
fullChain = []
iList = []
maxLength = 0
for i in range(1,1000000):
	iList.append(i)
	fullChain = []
	fullChain.append(i)
	#startNumb = i
	chainNumb = i
	while chainNumb > 1:
		if chainNumb % 2 ==0: 
			chainNumb = chainNumb/2
		else: 
			chainNumb = 3*chainNumb + 1
		fullChain.append(chainNumb)
	allFullChains.append(fullChain)
	#print allFullChains
for element in allFullChains: 
	if len(element) > maxLength:
		maxList = element
		maxLength = len(element)
longestIndex =  allFullChains.index(maxList)
#print allFullChains.index(maxList)
#print longestIndex
print iList[longestIndex]
#print maxLength

	





	