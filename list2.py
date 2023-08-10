# match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

def match_ends(string):
    count = 0
    for s in string:
        if (len(s) >=2) and (s[0] == s[-1]):
            count +=1 
    return count
            
string = ["aaa","bbc","cnc","xxxxxxx"]
result = match_ends(string)
print(result)


#Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

def linear_merge(list1, list2):
    merge_list = []
    len1 = len(list1)
    len2 = len(list2)
    i , j =  0,0
    
    while i<len1 and j<len2:
        if list1[i] < list2[j]:
            merge_list.append(list1[i])
            i += 1
        else:
            merge_list.append(list2[j])
            j += 1
        
    if i<len1 :
        merge_list.extend(list1[i:])
    if j<len2:
        merge_list.extend(list2[j:])
    
    return merge_list
        
list1 = [1,3,5,7]
list2 = [2,4,6,8]
result = linear_merge(list1,list2)
print(result)


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


def main():
    print (match_ends)
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print (linear_merge)
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
