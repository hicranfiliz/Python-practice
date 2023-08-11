# monkey trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling.
# Return True if we are in trouble. 

def monkey_trouble(a,b):
    if (a and b) or (not a and not b):
        return True
    else:
        return False


# positive negative
# Given 2 int values, return True if one is negative and one is positive.
# Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
    if negative:
        return a<0 and b<0
    else:
        return (a<0 and b>0) or (a>0 and b<0)
        
        
# count nine
# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    count = nums.count(9)
    return count
    
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print ('monkey_trouble')
    test(monkey_trouble(True, True), True)
    test(monkey_trouble(False, False), True)
    test(monkey_trouble(True, False), False)
    
    print
    print ('pos_neg')
    test(pos_neg(1, -1, False), True)
    test(pos_neg(-1, 1, False), True)
    test(pos_neg(-4, -5, True), True)
    
    print
    print ('array_count9')
    test(array_count9([1, 2, 9]), 1)
    test(array_count9([1, 9, 9]), 2)
    test(array_count9([1, 9, 9, 3, 9]), 3)


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
        
