# 4
import numpy as np

#4.1
arr = np.array([1, 3, 4, 5])
print(arr)

#4.1.1
A = np.array([[1, 2, 3], [7, 8, 9]])
print(A)
A = np.array([[1, 2, 3],[7, 8, 9]])
print(A)
A = np.array([[1, 2, \
               3],
[7, 8, 9]])
print(A)

#4.1.2
v = np.arange(1,7)
print(v,"\n")
v = np.arange(-2,7)
print(v,"\n")
v = np.arange(1,10,3)
print(v,"\n")
v = np.arange(1,10.1,3)
print(v,"\n")
v = np.arange(1,11,3)
print(v,"\n")
v = np.arange(1,2,0.1)
print(v,"\n")
v = np.linspace(1,3,4)
print(v)
v = np.linspace(1,10,4)
print(v)

X = np.ones((2,3))
Y = np.zeros((2,3,4))
Z = np.eye(2) # np.eye(2,2) # np.eye(2,3)
Q = np.random.rand(2,5) # np.round(10*np.random.rand((3,3)))
print(X,"\n\n",Y,"\n\n",Z,"\n\n",Q)

#4.1.3
U = np.block([[A], [X,Z]])
print(U)

#4.1.4
V = np.block([[
np.block([
np.block([[np.linspace(1,3,3)],[
        np.zeros((2,3))]]) ,
np.ones((3,1))])
],
[np.array([100, 3, 1/2, 0.333])]] )
print(V)

#4.2
print( V[0,2] )
print( V[3,0] )
print( V[3,3] )
print( V[-1,-1] )
print( V[-4,-3] )
print( V[3,:] )
print( V[:,2] )
print( V[3,0:3] )
print( V[np.ix_([0,2,3],[0,-1])] )
print( V[3] )

#4.3
Q = np.delete(V, 2, 0)
print(Q)
Q = np.delete(V, 2, 1)
print(Q)
v = np.arange(1,7)
print( np.delete(v, 3, 0) )

#4.4
np.size(v)
np.shape(v)
np.size(V)
np.shape(V)

#4.5.1
A = np.array([[1, 0, 0],[2, 3, -1],[0, 7, 2]] )
B = np.array([[1, 2, 3],[-1, 5, 2],[2, 2, 2]] )
print( A+B )
print( A-B )
print( A+2 )
print( 2*A )

#4.5.2
MM1 = A@B
print(MM1)
MM2 = B@A
print(MM2)

#4.5.3
MT1 = A*B
print(MT1)
MT2 = B*A
print(MT2)

#4.5.4
DT1 = A/B
print(DT1)

#4.5.5
C = np.linalg.solve(A,MM1)
print(C) # porownaj z macierza B
x = np.ones((3,1))
b =  A@x
y = np.linalg.solve(A,b)
print(y)

#4.5.6
PM = np.linalg.matrix_power(A,2) # por. A@A
PT = A**2  # por. A*A

#4.5.7
A.T # transpozycja
A.transpose()
A.conj().T # hermitowskie sprzezenie macierzy (dla m. zespolonych)
A.conj().transpose()

#4.6
A == B
A != B
2 < A
A > B
A < B
A >= B
A <= B
np.logical_not(A)
np.logical_and(A, B)
np.logical_or(A, B)
np.logical_xor(A, B)
print( np.all(A) )
print( np.any(A) )
print( v > 4 )
print( np.logical_or(v>4, v<2))
print( np.nonzero(v>4) )
print( v[np.nonzero(v>4) ] )

#4.7
print(np.max(A))
print(np.min(A))
print(np.max(A,0))
print(np.max(A,1))
#flatten nie dziła dla F
