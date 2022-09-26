import statistics

def multiplyList(myList):

	result = 1
	for x in myList:
		result = result * x
	return result


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

print("The product of the elements in 1 list =", multiplyList(list1))
print("The product of the elements in 2 list =", multiplyList(list2))
print("The product of the elements in 3 list =", multiplyList(list3))

print("The arithmetic mean of 1 list =", statistics.mean(list1))
print("The arithmetic mean of 2 list =", statistics.mean(list2))
print("The arithmetic mean of 3 list =", statistics.mean(list3))