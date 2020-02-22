#find all prime nums in b/w given numbers

start=input('enter starting number: ')
end=input('enter ending number: ')

for val in range(start, end +1):

#if num is divisible by any number
#b/w 2 and val, it is not prime

	if val > 1:
		for n in range(2, val):
			if (val % n) == 0:
				break
		else:
			print(val)

