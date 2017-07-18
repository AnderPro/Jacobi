

import numpy 
from pprint import pprint
from numpy import array, zeros, diag, diagflat, random

n=4

A=numpy.random.randint(10,size=(n,n))

b = numpy.random.randint(10,size=(n))

x0 = numpy.random.randint(10,size=(n))
x1 = numpy.zeros(n)

def Resto(A):
    
    D1=diag(A)
    R = A - diagflat(D1)
    return (R)

def diagonal(A):
	D=[]
	i=0
	j=0
	for i in range(n):
		D.append([])
		for j in range (n):
			if i==j:
				D[i].append(A[i][j])
			else:
				D[i].append(0)
	D = numpy.array(D)
	return (D)

def Dinversa(D):
	matriz=[]
	i=0
	j=0
	for i in range(n):
		matriz.append([])
		for j in range (n):
			if i==j:
				matriz[i].append(1/float((D[i][j])))
			else:
				matriz[i].append(0)
	matriz = numpy.array(matriz)
	return (matriz)



print "MATRIZ A"
pprint (A)
print "Terminos Independientes"
pprint (b)
print "X0:"
print x0
print "X1:"
print x1


D = diagonal(A)
print('D = ')
pprint (D)

R=Resto(A)
print('R = ')
pprint  (R)

while(numpy.array_equal(x0,x1)==False):
	x1=numpy.matmul((b-(numpy.matmul(x0,R))),Dinversa(D))
	x0=x1
print('soluciones= ')
pprint(x1)












