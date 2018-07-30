## 0/1 knapsack problem

import numpy as np

## w: weight
## v: value
## po: position of the pointer
## ca: capacity
w = [1,2,4,2,5]
v = [5,3,5,3,2]
po = 0
ca = 10



## === bottom up
## best way

## stores the values. 
memo2 = np.zeros([ len(w), ca+1], int)
# print(memo2)

## stores the best combinations to go into the knapsack
items = np.empty([ len(w), ca+1], dtype=object)

def ks_bu(weight, value, c):
	global memo2, items

	for w_pointer in range(len(weight)):
		## start from 1. the 1st is always 0 as the capacity is 0 and can't take anything
		## c_pointer: the capacity level. a pointer from 1 to c
		for c_pointer in range(1, c+1):
			## for the first row
			if w_pointer == 0:
				## just loop thru til the knapsack can take it
				if c_pointer >= weight[w_pointer]:
					## store the value of the item
					memo2[w_pointer][c_pointer] = value[w_pointer]

					## store the index of the item
					items[w_pointer][c_pointer] = str(w_pointer) +','

			## 2nd row onward
			else:
				## if can't take this item
				if c_pointer < weight[w_pointer]:
					## copy the last best value at 1 row up
					memo2[w_pointer][c_pointer] = memo2[w_pointer-1][c_pointer]
					
					## copy the last best combination at 1 row up
					items[w_pointer][c_pointer] = items[w_pointer-1][c_pointer]
				## if can take this item
				else:
					## if take the item
					temp1 = value[w_pointer] + memo2[ w_pointer-1 ][ c_pointer- weight[w_pointer] ]

					## if not take the item
					temp2 = memo2[w_pointer-1][c_pointer]

					memo2[w_pointer][c_pointer] = max(temp1, temp2)

					## if taking the item
					if temp1 > temp2:
						## add the item into the combination
						items[w_pointer][c_pointer] = items[ w_pointer-1 ][ c_pointer- weight[w_pointer] ] + str(w_pointer) + ','
					else:
						## copy the best combination at 1 row up
						items[w_pointer][c_pointer] = items[ w_pointer-1 ][ c_pointer ]
	print('Final [][] of value: ')
	print(memo2)
	print('Final [][] of combination: ')
	print(items)
	print('Taking the items at: ', (items[len(w)-1][ca])[:-1])
	return memo2[len(weight)-1, c]

print('Bottom up => Total value of best combo: ', ks_bu(w, v, ca))
## === bottom up





## === recursion

## memo of the best sum value at the capacity [c]
memo = np.ones([ len(w), ca+1], int)
memo = memo * -1
# print(memo)

## pointer: position of the pointer at the item (w) array
## c_remain: remaining capacity

## left to right
## top down approach
## return the best value
def ks(weight, value, pointer, c_remain):
	global memo

	## if the best value is already calculated, return it without calculating again
	if memo[pointer][c_remain] != -1:
		return memo[pointer][c_remain]

	## if reached the end of the items or no capacity left
	if pointer == len(weight)-1 or c_remain == 0:
		## best value is 0 since we cant put any more thing into the knapsack
		result = 0
	## if adding the [n] item exceed the remaining capacity
	elif weight[pointer] > c_remain:
		## move to next item
		result = ks(weight, value, pointer+1, c_remain)
	else:
		## try choosing a better item

		## if not take the item
		temp1 = ks(weight, value, pointer+1, c_remain)

		## if take the item
		temp2 = value[pointer] + ks(weight, value, pointer+1, c_remain - weight[pointer])

		result = max(temp1, temp2)

	## save the calculated result
	memo[pointer][c_remain] = result
	# print(memo)
	return result

print('Top down => Total value of best combo: ', ks(w, v, po, ca))
## === recursion
