#  Sieve of Eratosthenes - The sieve of Eratosthenes 
# is one of the most efficient ways to find all of 
# the smaller primes (below 10 million or so).

Number = int(input('insert number where we should find all the prime numbers to'))
list_number = list(range(Number))
del list_number[0]
del list_number[0]

#to check on range of numbers
# print(list_number)  

keeprunning = True
print('your prime numbers are :')
while keeprunning:

    try:
        y= list_number.pop(0)
        print(y)

    except:
        keeprunning = False
        

    for x in list_number:
        if x % y == 0:
            list_number.remove(x)

