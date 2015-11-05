numbers = [7,3,1,6,7,1,7,6,5,3,1,3,3,0,6,2,4,9,1,9,2,2,5,1,1,9,6,7,4,4,2,6,5,7,4,7,4,2,3,5,5,3,4,9,1,9,4,9,3,4,
9,6,9,8,3,5,2,0,3,1,2,7,7,4,5,0,6,3,2,6,2,3,9,5,7,8,3,1,8,0,1,6,9,8,4,8,0,1,8,6,9,4,7,8,8,5,1,8,4,3]
endAll = len(numbers)/13
startAmount = 0
#print startAmount
newListVar = 0
numProd = 1
x = 0 

for i in range(0,endAll):
	thirteenNum = []
	for i in range(startAmount, startAmount+13):
		checkProd = 1
		thirteenNum.append(numbers[i]) 	
		for element in thirteenNum:
			#if x in thirteenNum: 
				#break
			#else: 	
			checkProd *= element
	print checkProd
	if checkProd > numProd:
		print "greater"
		numProd = checkProd
	else:
		print "not greater"
	print thirteenNum
	startAmount+=13







