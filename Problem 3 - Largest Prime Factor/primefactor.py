number_to_factorize = 600851475143
largest_factor = -1

i = 2
primeFound = False

while i < number_to_factorize:
	if number_to_factorize%i == 0:
		factor = number_to_factorize/i
		print str(factor) + " and " + str(i) + " Is a factor of " + str(number_to_factorize) 
		if (factor < 17425170):
			isPrime = True
			for j in range(2, factor):
				if factor % j == 0:
					isPrime = False
					break
			
			if isPrime:
				largest_factor = factor
				primeFound = True
	
	if primeFound:
		break
	i = i+1
	
print "The largest prime factor is " + str(largest_factor)
	
				

		