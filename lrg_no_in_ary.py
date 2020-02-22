#python prog to fnd max num in array
def largest(arr,n):
	max = arr[0]

	for i in range(1,n):
		if arr[i] > max:
			max = arr[i]
	return max

arr=input('enter a array: ')
n= len(arr)
Ans = largest(arr,n)
print 'largest in given array is',Ans
