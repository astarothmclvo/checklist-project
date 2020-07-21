s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5

print("The next five characters are '%s'" % s[5:10]) # 5 to 10

print("The thirteenth character is '%s'" % s[12]) # Just number 12

print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)

print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

print("Reversed String '%s'" % s[::-1]) #Reversed String 

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

#Join a Strings 
astring1 = "Hello, my name is: "
astring2 = "Marco"

print(astring1.join(astring2))

print(' '.join({astring1,astring2}))

print(' '.join([astring1,astring2]))

#String Format
'{first} {last}'.format(first='Hodor', last='Hodor!')

print("The age of {0} is {1}. {0}'s birthday is on {2}".format('Marco', 30, 'October 29'))       

import math

print("Math constants: pi={m.pi}, e={m.e}".format(m=math))

print("Math constants: pi={m.pi:.3f}, e={m.e:.3f}".format(m=math))

def isPalindrome(aux):
    if aux == aux[::-1]:
        print("The word '%s' is a Palindrome" % aux)
    else:
        print("The word '%s' is not a Palindrome" % aux)

isPalindrome("arribalabirra")

def isEven(numb):
    if numb % 2 == 0:
        print("The number %d is an Even number" % numb)
    else:
        print("The number %d is not an Even number" % numb)

def isEvenBoolean(numb):
    if numb % 2 == 0:
       return True
    else:
        return False

print(isEvenBoolean(4))

def sumEven(n):
    summatory = 0
    for i in range(0, int(n)):
        if(isEvenBoolean(i)):
            summatory = summatory + i
    
    print("The summary of even numbers from 0 to {0} =  is {1} ".format(n, summatory))

sumEven(100)     
  
##Exercise Calculate the summatory for Odd numbers
# 
# #


from math import sqrt

def quadraticFunction(a, b, c):
    print("Quadratic function for : ({0}* x^2) + {1}*x + {2}".format(a,b,c))

    d = b**2 - 4*a*c

    if d > 0:
        num_roots = 2
        x1 = (((-b) + sqrt(d))/(2*a))     
        x2 = (((-b) - sqrt(d))/(2*a))
        print("There are 2 roots: {0} and {1}".format(x1, x2))
    elif d == 0:
        num_roots = 1
        x = (-b) / 2*a
        print("There is one root: ", x)
    else:
        num_roots = 0
        print("No roots, discriminant < 0.")
        exit()

quadraticFunction(1,0,-1)

##Excercise Create a function that Calculates the area of an redctangle shape and determine if it is an square 

fruits = ["apple", "banana", "cherry"]
while fruits:
    print(fruits.pop(-1))

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

a = ['foo', 'bar', 'baz']
while True:
    if not a:
        break
    print(a.pop(-1))

## 25$ Amazon gift card Bonus Exercise for the first MenTe that resolve the following problem:
# Create a Function thar calculates the area of an Acre according the British colonial mesuarments units 
# The formula is on the following video https://www.youtube.com/watch?v=m55RDNlWnLI 
#The Answer Code Must be on my email before 12 am astarothmcvlo@gmail.com 