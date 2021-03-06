# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
#By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
#find the sum of the even-valued terms.

max_number = 4000000

fib_n_minus_1 = 1
fib_n = 2

sum = fib_n

while (fib_n + fib_n_minus_1) < max_number:
	temp = fib_n
	fib_n = fib_n + fib_n_minus_1
	fib_n_minus_1 = temp
	
	if fib_n%2 == 0:
		sum += fib_n
		
print sum
	