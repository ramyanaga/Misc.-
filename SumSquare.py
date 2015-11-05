sumSquare = 0 
squareSum = 0
sumDiff = 0
for i in range (1,101): 
	sumSquare += i 
sumSquare *= sumSquare
print sumSquare 

for i in range(1,101): 
	iP2 = i * i 
	squareSum += iP2
print squareSum
sumDiff = sumSquare - squareSum
print sumDiff