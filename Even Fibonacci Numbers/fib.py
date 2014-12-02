
fibn1 = 1
fibn = 2

sum = fibn

while (fibn + fibn1) < 4000000:
	temp = fibn
	fibn = fibn + fibn1
	fibn1 = temp
	
	if fibn%2 == 0:
		sum += fibn
		
print sum
	