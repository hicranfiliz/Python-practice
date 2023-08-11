# a Python function that takes a number as a parameter and check the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself. 

def isPrime(number):
    if number > 1:
        for i in range(2,number):
            if (number % i == 0):
                return False
            else:
                return True
    else:
        return False
            
number = int(input("Enter a number: "))

if isPrime(number):
    print("{} is a prime number".format(number))
else:
    print("{} is not a prime number".format(number))
    
    
    
# multiply_3_5
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below n.

def multiply_3_5(n):
    sum = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i
    return sum
    
n = int(input("Enter a number: "))
result = multiply_3_5(n)
print(result)

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return. 

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


        # Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print(isPrime)
    test(isPrime(1), False)
    test(isPrime(23), True)
    test(isPrime(77), False)
    
    print
    print (multiply_3_5)
    test(multiply_3_5(10), 23)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
        
