#! /usr/bin/python

'''
https://blog.svpino.com/2015/05/10/programming-challenge-rotating-a-matrix-90-degrees-in-place
Write a function to rotate an NxN matrix by 90 degrees.
You should rotate it in place, meaning you can't use another matrix to perform the rotation,
but instead you have to use the same given structure.
'''

def transform(trix):
    count = 1
    stub = 0
    for y, row in enumerate(trix):
        for x, val in enumerate(row, stub):
            if count == len(trix)*len(row) / 4 + 1:
                print count
                return trix
            if x == len(row) -1 - stub:
                break
            hold = row[x]
            row[x] = trix[-1-x][y]
            trix[-1-x][y] = trix[-1-stub][-1-x]
            trix[-1-stub][-1-x] = trix[x][-1-y]
            trix[x][-1-y] = hold
            count += 1
        #return ['']
        stub += 1

def matBuild(size):
    mat = []
    count = 1
    while len(mat) < size:
        row = []
        while len(row) < size:
            row.append(count)
            count += 1
        mat.append(row)
    return mat

if __name__ == '__main__':
    mat = matBuild(10)
    for row in mat:
        print row
    print '\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/'
    for row in transform(mat):
        print row
    
    print
    print
