#  Sieve of Eratosthenes - The sieve of Eratosthenes 
# is one of the most efficient ways to find all of 
# the smaller primes (below 10 million or so).

#to change to function   def prime(Number):
Number = int(input('insert number where we should find all the prime numbers to'))
list_number = list(range(Number))
list_number.pop(0)
list_number.pop(0)

#to check on range of numbers
# print(list_number)  

prime_numbers = []
keeprunning = True
while keeprunning:

    try:
        y = list_number.pop(0)
        prime_numbers.append(y)
    except:

        print(f'these are your prime numbers {prime_numbers}' )
        keeprunning = False
        #for function return prime_numbers

    for x in list_number:
        if x % y == 0:
            z = list_number.index(x)
            list_number.pop(z)

        
        
