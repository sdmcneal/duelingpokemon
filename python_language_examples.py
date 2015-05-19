#!/usr/bin/env python
#
# --------------------------------------------------
# Examples of common python 3 programming structures
# --------------------------------------------------
#

#
# conditionals and string formatting
#

# assign multiple variables
a, b = 4,9

# use conditional to test
if a < b:
    # {} are replaced by the arguments in .format(x,y)
    print('a({}) is less than b({})'.format(a,b))
else:
    print('a({}) is not less than b({})'.format(a,b))

# another way to do a conditional
print("a is less than b" if a < b else "a is not less than b")

#
# looping values
#

# while
c = 1
while c < 25:
    print('c={}'.format(c))
    c = c + 5
    
# iterators
d = ['first','second','third']
for i in d:
    print(i)
    
    
#
# functions
#
print("*** Functions ***")

def isprime(n):
    if n == 1:
        print('1 is special')
        return False
    for x in range(2,n):
        if n % x == 0:
            print('{} equals {} x {}'.format(n,x,n//x))
            return False
    else:
        print(n,'is a prime number')
        return True
    
for n in range(1,20):
    isprime(n)