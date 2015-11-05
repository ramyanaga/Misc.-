"""
1 2 3 4 5 
2 4 6 3 7 
9 1 8 4 2 
6 5 3 2 8 
3 5 4 6 7 
""" 
row_1 = [1,2,3,4,5]
row_2 = [2,4,6,3,7]
row_3 = [9,1,8,4,2]
row_4 = [6,5,3,2,8]
row_5 = [3,5,4,6,7]
all_rows = [row_1, row_2,row_3,row_4,row_5]

def calculate_horizontal(list):
	largest_product = 1
	for i in all_rows:
		#test_product = 1
		for j in i: 
			test_product = j * (j+1)
			if test_product > largest_product: 
				largest_product = j * (j+1)
				biggest_num = j 
	print biggest_num			
	print largest_product
			#largest_product = 1

if __name__=='__main__':
	row_1 = [1,2,3,4,5]
	row_2 = [2,4,6,3,7]
	row_3 = [9,1,8,4,2]
	row_4 = [6,5,3,2,8]
	row_5 = [3,5,4,6,7]
	all_rows = [row_1, row_2,row_3,row_4,row_5]
	calculate_horizontal(all_rows)


		
