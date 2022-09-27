import numpy

def sumNMean(arr):
    newlist = list(map(int, arr.split()))
    sum1 = sum(newlist)
    mean = numpy.mean(newlist)
    print("array",newlist,",sum of elements:",sum1,".Mean :",mean)


n = int(input("enter the number of arrays:"))

arr = []
for i in range(n):
    arr.append(input("enter the array :"))

for i in range(n):
    sumNMean(arr[i])
