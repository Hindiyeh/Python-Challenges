#Happy Numbers - A happy number is defined by the following process. 
# Starting with any positive integer, replace the number by the sum 
# of the squares of its digits
# ,and repeat the process until the number equals 1 (where it will stay), 
# or it loops endlessly in a cycle which does not include 1. 
# Those numbers for which this process ends in 1 are happy numbers, 
# while those that do not end in 1 are unhappy numbers. 
# Display an example of your output here. Find first 8 happy numbers.

#assign the starting value
keeprunning = True
trys = 0
try:
    starting_value = int(input('type any positive integer'))
except:
    print('you motherfucker type an integer')
total_value = 0
starting_value_lst = list(str(starting_value))
starting_value_2 = []

while keeprunning:

    trys = trys + 1
    for i in starting_value_lst:
        i = (int(i))**2
        starting_value_2.append(i)

    for i in range(len(starting_value_2)):
        total_value += starting_value_2[i]

    if total_value == 1:
        print(f'your number is a happy number which is {starting_value}')
        keeprunning = False
    elif trys == 1000:
        print(f'your number is not a happy number we did 1000 iterations of  {starting_value} to reach {total_value}')
        keeprunning = False
    
    starting_value_lst = list(str(total_value))
    starting_value_2 = []
    total_value = 0