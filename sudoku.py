import numpy as np
import copy

"""
	Sudoku 
	Brute force recursion depth first 
"""

def search (a_):

    a = copy.deepcopy(a_)

    seq = [1,2,3,4,5,6,7,8,9]

    for y in xrange(9):
        for x  in xrange(9):
            if a[y,x] == 0:
                for n in xrange(1, 10):
                    if (n in a[y:y+1] or n in a[:,x]):
			continue
                    a[y,x] = n
                    search(a)
                return

    if (all((np.sort(a[0:3,0:3].reshape(1,9)) == seq)[0]) and
	all((np.sort(a[0:3,3:6].reshape(1,9)) == seq)[0]) and
	all((np.sort(a[0:3,6:9].reshape(1,9)) == seq)[0]) and
	all((np.sort(a[3:6,0:3].reshape(1,9)) == seq)[0]) and
	all((np.sort(a[3:6,0:3].reshape(1,9)) == seq)[0]) and
	all((np.sort(a[3:6,0:3].reshape(1,9)) == seq)[0]) and
	all((np.sort(a[6:9,0:3].reshape(1,9)) == seq)[0]) and
	all((np.sort(a[6:9,3:6].reshape(1,9)) == seq)[0]) and
	all((np.sort(a[6:9,6:9].reshape(1,9)) == seq)[0])):
	print(a)
"""
a= np.array((
	(5,6,0,0,9,3,0,0,0),
	(0,4,0,8,7,2,3,0,0),
	(3,0,0,0,4,0,0,2,0),
	(0,8,0,0,0,9,0,5,6),
	(0,5,6,7,2,0,4,0,0),
	(0,0,9,0,3,6,0,0,0),
	(0,1,0,0,0,0,8,0,9),
	(0,0,0,0,0,0,0,0,0),
	(8,0,0,0,0,0,0,0,7)))
"""

a= np.array((
	(0,0,1,0,8,2,6,9,5),
	(0,0,5,3,6,7,0,0,1),
	(0,0,0,1,9,5,0,4,0),
	(0,5,0,0,0,0,0,0,3),
	(0,0,8,2,0,4,0,5,6),
	(0,0,2,9,0,0,1,8,0),
	(2,0,0,0,0,0,5,0,0),
	(0,0,3,0,0,9,0,6,0),
	(0,0,9,0,0,6,0,0,0)))
print(a)
print ("----")

search(a)
