triangleSums = [0,1] 

for i in range(2,100000):
	triangleNewSum = triangleSums[i-1] + i 
	#print triangleNewSum 
	triangleSums.append(triangleNewSum)
	print len(triangleSums)
	if len(triangleSums) > 499: 
		break
	