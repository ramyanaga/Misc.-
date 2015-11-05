from datetime import datetime
def calc1(limit): 
	allFullChains = []
	fullChain = []
	iList = []
	maxLength = 0
	for i in range(1,limit):
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
	print iList[longestIndex]

def calc2(limit): 
	iList = []
	maxLength = 0
	fullChainLengths = []
	for i in range(1,limit):
		iList.append(i) 
		iTicker = 0
		chainNumb = i
		while chainNumb > 1:
			if chainNumb % 2 ==0: 
				chainNumb = chainNumb/2
			else: 
				chainNumb = 3*chainNumb + 1
			iTicker+=1
		fullChainLengths.append(iTicker)
	#print fullChainLengths
	for element in fullChainLengths:
		if element > maxLength:
			maxLength = element
	#print maxLength
	maxLengthIndex = fullChainLengths.index(maxLength)
	#print maxLengthIndex
	print iList[maxLengthIndex]


def calc3(limit):
	iList = []
	maxLength = 0
	fullChainLengths = [1]
	for i in range(1,limit):
		iList.append(i)
		iTicker = 0
		chainNumb = i
		while chainNumb > 1: 
			if chainNumb % 2 == 0:
				if chainNumb == 2: 
					break
				else: 
					chainNumb = chainNumb/2
			else:
				chainNumb = 3*chainNumb + 1
			iTicker+=1
		fullChainLengths.append(iTicker)
	for element in fullChainLengths:
		if element > maxLength:
			maxLength = element	
	maxLengthIndex = fullChainLengths.index(maxLength)
	print iList[maxLengthIndex]		


if __name__ == "__main__":
	"""
	start1 = datetime.now()
	calc1(1000000)
	end1 = datetime.now()
	print end1 - start1
	"""
	
	start2 = datetime.now()
	calc2(1000)
	end2 = datetime.now()
	print end2 - start2

	start3 = datetime.now()
	calc3(1000)
	end3 = datetime.now()
	print end3 - start3


	





	