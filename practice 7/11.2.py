list1 = [10, 250, 20, 4, 100, 45, 99]

print(list1)
print("maximum of 1st list:", max(list1))

list2 = [15, 86, 54, 320, 112, 55, 74]

print(list2)
print("maximum of 2nd list:", max(list2))

index1 = list1.index(max(list1))
index2 = list1.index(max(list2))

list1[index1], list2[index2] = list2[index2], list1[index1]

print(list1, list2)
