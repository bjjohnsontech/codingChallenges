#! /usr/bin/python
'''
These are five programmin challenges every developer should be able to do in under an hour.
https://blog.svpino.com/2015/05/07/five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
'''

def problem1(l):
    '''
    Write three functions that compute the sum of the numbers in a given list using a for-loop, a while-loop, and recursion.
    '''
    print for1(list(l))
    print while1(list(l))
    print rec1(list(l))
    
def for1(lis):
    total = 0
    for i in lis:
        total += i
    return total

def while1(lis):
    total = 0
    while lis:
        total+=lis.pop()
    return total

def rec1(lis):
    total = lis.pop()
    if lis:
        #print lis
        total += rec1(lis)
    return total

def problem2(a,b):
    '''
    Write a function that combines two lists by alternatingly taking elements. For example: given the two lists [a, b, c] and [1, 2, 3], the function should return [a, 1, b, 2, c, 3].
    '''
    new = []
    i=0
    while i<len(a) or i<len(b):
        try:
            new.append(a[i])
        except:
            pass
        try:
            new.append(b[i])
        except:
            pass
        i+=1
    print new
    
def problem3():
    '''
    Write a function that computes the list of the first 100 Fibonacci numbers. By definition, the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two. As an example, here are the first 10 Fibonnaci numbers: 0, 1, 1, 2, 3, 5, 8, 13, 21, and 34.
    '''
    fibs = [0,1]
    while len(fibs)<100:
        fibs.append(fibs[-1]+fibs[-2])
    print fibs

def problem4(lis):
    '''
    Write a function that given a list of non negative integers, arranges them such that they form the largest possible number. For example, given [50, 2, 1, 9], the largest formed number is 95021.
    '''
    new = [lis.pop()]
    while lis:
        num = lis.pop()
        for x, item in enumerate(new):
            numL = len(str(num))
            iL = len(str(item))
            if numL == iL: # same number of digits in numbers
                numCmp = num
                iCmp = item
            elif numL < iL: # new number is shorter than item
                numCmp = num
                iCmp = int(str(item)[0:numL]) # only comparing the same length part
            elif numL > iL: # new number is longer than item
                numCmp = int(str(num)[0:iL]) # only comparing same length part
                iCmp = item
            # 9 == (9)0 and shorter so goes in front
            # 9 > (8)9 so goes in front
            if numCmp > iCmp or(numCmp == iCmp and numL < iL):
                new.insert(x, num)
                break
        else:
            new.append(num)
    #print new
    print ''.join(str(x) for x in new)

def problem5(nums, huh, b, e, sols):
    '''
    Write a program that outputs all possibilities to put + or - or nothing between the numbers 1, 2, ..., 9 (in this order) such that the result is always 100. For example: 1 + 2 + 34 - 5 + 67 - 8 + 9 = 100.'''
    while e<10:
        it = ''.join(nums[b:e])
        i = -1
        while i<2:
            huh.append(i*int(it))
            huh, sols = problem5(nums, huh, e, e+1, sols)
            if e==9:
                #huh[0] = huh[0]
                #print huh
                if sum(huh) == 100 and huh[0] != -1:
                    p = ''
                    for x, item in enumerate(huh):
                        if item > 0 and x != 0:
                            sign = '+'
                        else:
                            sign = ''
                        p += sign
                        p += str(item)
                    sols.append(p)
            huh = huh[0:-1]
            i+=2
        e+=1
    return huh, sols

    
if __name__ == '__main__':
    print 'Problem 1 solutions:'
    problem1([1,1,1,1])
    print 'Problem 2 solution:'
    problem2(['a','b','c','d','e'],[1,2,3,4,5,6,7])
    print 'Problem 3 solutions:'
    problem3()
    print 'Problem 4 solution:'
    problem4([9, 90, 93, 5, 6, 1, 2, 23, 39, 29])
    print 'Problem 5 solutions:'
    print '\n'.join(problem5(['1','2','3','4','5','6','7','8','9'], [], 0, 1, [])[1])
