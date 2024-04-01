import numpy as np
from numpy.fft import fft, ifft
from math import floor,sqrt



def divisors(n): #O(n^1/2)
	divs = [1]
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			divs.extend([i,int(n/i)])
	divs.extend([n])
	return (list(set(divs)))

#https://www.geeksforgeeks.org/generate-unique-partitions-of-an-integer/
#Unique partitions of an integer O(n*k) = O(2n)
# A utility function to print an
# array p[] of size 'n'
def printArray(p, n):
	m=[]
	for i in range(0, n):
		#print(p[i], end = " ")
		m.append(p[i])
	#print()
	return m

def printAllUniqueParts(n):
	p = [0] * n	 # An array to store a partition
	k = 0		 # Index of last element in a partition
	p[k] = n	 # Initialize first partition
				# as number itself
	P=[]
	# This loop first prints current partition, 
	# then generates next partition.The loop 
	# stops when the current partition has all 1s
	while True:
		# print current partition
		if k+1==2:
			P.append(printArray(p, k + 1))

		# Generate next partition

		# Find the rightmost non-one value in p[]. 
		# Also, update the rem_val so that we know
		# how much value can be accommodated
		rem_val = 0
		while k >= 0 and p[k] == 1:
			rem_val += p[k]
			k -= 1

		# if k < 0, all the values are 1 so 
		# there are no more partitions
		if k < 0:
			#print()
			return P

		# Decrease the p[k] found above 
		# and adjust the rem_val
		p[k] -= 1
		rem_val += 1

		# If rem_val is more, then the sorted 
		# order is violated. Divide rem_val in 
		# different values of size p[k] and copy 
		# these values at different positions after p[k]
		while rem_val > p[k]:
			p[k + 1] = p[k]
			rem_val = rem_val - p[k]
			k += 1

		# Copy rem_val to next position 
		# and increment position
		p[k + 1] = rem_val
		k += 1
	return P




def gcdExtended(a, b): #O(logn)
	if a == 0:
		return b, 0, 1
	gcd, x1, y1 = gcdExtended(b % a, a) 
	x = y1 - (b//a) * x1
	y = x1
	return (gcd,x,y)


def get_sum_mul_decomp(N):
	a = [x for x in range(1,N+1)]
	s = printAllUniqueParts(N)
	y = [x for x in range(1,N+1)]
	mult=[]
	for x in range(len(s)):  #O(n/2)
		first = s[x][0]
		second= s[x][1]
		ma=0
		ma1=0
		g = list(divisors(first))
		g1 = list(divisors(second)) #O(n^1/2)
		for w in g:
			(gcd,x,r) = gcdExtended(first,w)
			ma = int(max(ma,gcd/first))
		for w in g1:
			(gcd2,x2,r2) = gcdExtended(second,w)
			ma1= int(max(ma1,gcd2/second))
		mult.append([[first,ma],[second,ma1]])
	return mult

def create_tuples(m): #O(n)
	tuplas=[]
	for x in range(len(m)):
		a=m[x][0][0]
		b=int(m[x][0][1])
		c=m[x][1][0]
		d=int(m[x][1][1])
		tuplas.append(tuple([a,b,c,d]))
	return tuplas

def maxima_tupla(t): #O(n)
	MAX=0
	(q,w,e,r) = tuple([MAX,MAX,MAX,MAX])
	for tupla in t:
		(a,b,c,d) = tupla
		if a>=q or b>=w or c>=e or d>=r:
			(q,w,e,r) = (a,b,c,d)
	return (q,w,e,r)

def decomp(N):
	mult_sum_decomp = get_sum_mul_decomp(N)
	X = create_tuples(mult_sum_decomp)
	maxim = maxima_tupla(X)
	print("La maxima tupla para X =",N,"es",maxim,"donde",maxim[0],"*",maxim[1],"+",maxim[2],"*",maxim[3],"=",N)

s = input("Introduce un número para calcular decomp(X), X=")
decomp(int(s))