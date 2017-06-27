#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
import copy

'''
	The Telegraph

	World's hardest sudoku
 
	http://www.telegraph.co.uk/news/science/science-news/9359579/Worlds-hardest-sudoku-can-you-crack-it.html
'''

def search (a_):

	a = copy.deepcopy(a_)
	
	for y in xrange(9):
		for x  in xrange(9):
			if a[y,x] == 0:
				r = range(1,10)
				r = [ i for i in r if i not in a[y:y+1] ]
				r = [ i for i in r if i not in a[:,x] ]
				r = [ i for i in r if i not in a[(y//3)*3:(y//3+1)*3,(x//3)*3:(x//3+1)*3] ]
				
				for n in r:
					a[y,x] = n
					search(a)
				return
	print (a)


a = np.array((
	(8,0,0,0,0,0,0,0,0),
	(0,0,3,6,0,0,0,0,0),
	(0,7,0,0,9,0,2,0,0),
	(0,5,0,0,0,7,0,0,0),
	(0,0,0,0,4,5,7,0,0),
	(0,0,0,1,0,0,0,3,0),
	(0,0,1,0,0,0,0,6,8),
	(0,0,8,5,0,0,0,1,0),
	(0,9,0,0,0,0,4,0,0)))
print(a)
print ("----")

search(a)
