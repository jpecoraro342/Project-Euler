# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

number_to_factorize = 600851475143
largest_factor = -1

i = 2
prime_found = False

while i < number_to_factorize:
	if number_to_factorize%i == 0:
		factor = number_to_factorize/i
		print str(factor) + " and " + str(i) + " Is a factor of " + str(number_to_factorize) 

		if (factor < 17425170):
			is_prime = True
			for j in range(2, factor):
				if factor % j == 0:
					is_prime = False
					break
			
			if is_prime:
				largest_factor = factor
				prime_found = True
	
	if prime_found:
		break
	i = i+1
	
print "The largest prime factor is " + str(largest_factor)
	
				

		