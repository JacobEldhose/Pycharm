# ===========1D iteration============

# interview qns:
# difference between linspace and arange
# difference between reshape and flatten
# interview qn:perform dot product(2d)
#sort,ceil,round

import numpy as np
a=np.array([4,5,8,1,2,3,4,9,6])
#=======2D iteration=============
a=np.array([[3,4,5,0],[5,10,7,4],[4,3,2,8],[7,2,3,4]])
print(a.shape)
print(a.size)
# dtype==>datatype of matrix
print(a.dtype)
print(a.ndim)
# difference between linspace and arange
# arange==>1.elements in the matrix will be from a defined range 2.applicable to only 1D
import numpy as np
a=np.arange(1,18)
# start ,stop
print(a)
a=np.arange(1,26)
print(a)
# linspace==all 3 values are must==>'num' is the no. of elements, diffence between elements will be same
import numpy as np
a=np.linspace(1,11,5)
print(a)
a=np.arange(1,26)
# 2D 5*5 matrix
# reshape concept vs flatten
d=np.array([[4,5,4,9],[8,7,9,5],[7,2,1,3]])
print(d)
# reshape is used to change order of a matrix===while reshaping,total elements should be same
print("*"*100)
b=d.reshape([4,3])
print(b)
f=d.reshape([12])
print(f)
b=a.reshape([5,5])
print(b)
# 3D  5*6 matrix
a=np.arange(1,31).reshape([1,5,6])
print(a)
# flatten is used to convert matrix to 1D matrix
import numpy as np
d=np.array([[4,5,4,9],[8,7,9,5],[7,2,1,3],[4,5,8,7]])
b=d.flatten()
print(b)

# =====>1D--argmax,max,min<=======
# returns index maximum value
a=np.array([4,5,6,0,14,8,7,10,11])
b=np.argmax(a)
print(b)
b=np.argmin(a)
print(b)
a=np.array([[3,4,5,0],[5,10,7,4],[4,3,2,8],[7,2,3,4]])
# column wise==max
b=np.argmax(a,axis=0)
print(b)
# row wise ==max
b=np.argmax(a,axis=1)
print(b)
# column wise==min
b=np.argmin(a,axis=0)
print(b)
# row wise ==min
b=np.argmin(a,axis=1)
print(b)
# argsort==>index of sorted list
a=np.array([4,5,6,0,14,8,7,10,11])
b=np.argsort(a)
print(b)
# 2D
a=np.array([[3,4,5,0],[5,10,7,4],[4,3,2,8],[7,2,3,4]])
# returns index
# by default ==row in ascending order
b=np.argsort(a)
print(b)
# ====>column wise<=======
b=np.argsort(a,axis=0)
print(b)
# mathematical Operations

a=np.array([[4,5,6],[1,2,3],[4,5,6]])
b=np.array([[8,9,6],[5,3,3],[9,4,6]])
#Addition===element by element==>order should be same
#[4,5,6]    [8,9,6]
# [1,2,3]   [5,3,3]
# [4,5,6]]  [9,4,6]]
s=np.add(a,b)
print(s)
#Subtraction===element by element==>order should be same
s=np.subtract(a,b)
print(s)
# Multiplication==element by element==>order should be same
s=np.multiply(a,b)
print(s)
#Division ==element by element==>order should be same
s=np.divide(a,b)
print(s)
# square()
s=np.square(a)
print(s)
# squareroot
s=np.sqrt(a)
print(s)
# interview q,n:perform dot product

a=np.array([4,5,6,1,2,3,4,5,6])
n=np.array([8,2,6,1,2,3,4,8,4])
# 1D-dot product==>one by one multiplication and sum it
c=np.dot(a,n)
print(c)
# 2D...>dot product-->row*column==>first matrix column ==second matrix row==>there is no need that order must be same
a=np.array([[[3,4,5],[5,8,7],[4,3,2]]])
b=np.array([[[5,4,8],[8,7,5],[8,7,6]]])
c=np.dot(a,b)
print(c)
# filter
import numpy as np
a=np.array([[3,4,5,0],[5,10,7,4],[4,3,2,8],[7,2,3,4]])
b=a%2==0
c=a[b]
print(c)
# floor==floor division==>to lowest integer
b=np.array([[[4.1,5.2,8.5],[8.2,4.4,5.2],[4.2,3.2,2.4],[4.2,5.9,1.6]]])
a=np.floor(b)
print(a)
# ceil==>same as floor division but to highest integer
a=np.ceil(b)
print(a)
# round==== >0.5==>to highest,<0.5===>to lowest      =0.5  even,to lowest else,to highest
a=np.round(b)
print(a)
# full matrix
# # default datatype: int
# all elements in the matrix are as defined by the user
# [3,3,3]
# [3,3,3]
import numpy as np
a=np.full([4,3],5)
print(a)
print(a.ndim)
# 1D,10elemts,no.7
# 3D,(4,5)elemts,no.3
a=np.full([10],7)
print(a)
print(a.ndim)
a=np.full([1,4,5],3)
print(a)
print(a.ndim)
#identity matrix -->diagonal element=1 and other elements are 0 AND square matrix-->(no. of columns=no. of rows)

# [1,0,0]
# [0,1,0]
# [0,0,1]

# [1,0]
# [0,1]

# [1,0,0]
# [0,1,0]
#[0,0,1]

# identity matrix is possible only in 2D
# # default datatype: float
# identity or eye function for identity matrix

import numpy as np
a=np.identity(3,dtype=int)
print(a)

import numpy as np
a=np.eye(3,dtype=int)
print(a)
# ===========>1D concatenation<=============
import numpy as np
a=np.array([4,5,8,1,2,3,4,9,6])
b=np.array([5,4,7,8,9,1,2,3,0])

#concatenate===>combine 2 matrix
c=np.concatenate((a,b))
print(c)

# =============>2D concatenation<==========
a=np.array([[3,4,5,0],[5,10,7,4],[4,3,2,8],[7,2,3,4]])
b=np.array([[7,2,3,4],[3,4,5,0],[5,10,7,4],[4,3,2,8]])
# by default  column wise
c=np.concatenate((a,b))
print(c)
# rowwise concatenation
c=np.concatenate((a,b),axis=1)
print(c)
# # default datatype: float
# ones matrix==all elements are 1
# [1,1,1]
# [1,1,1]
# [1,1,1]
import numpy as np
a=np.ones([4,3],dtype=int)
print(a)
print(a.ndim)
import numpy as np
a=np.ones([4],dtype=int)
print(a)
print(a.ndim)
import numpy as np
a=np.ones([1,4,3],dtype=int)
print(a)
print(a.ndim)
# 2D--4*5 matrix slicing
a=np.array([[4,8,5,6,8],[6,5,8,9,6],[4,5,8,2,3],[8,7,8,2,1]])
# print(a[row,column])
# row/column may contain start,stop,step
print(a[1:,:2])
# row==>1,2,3  column==>0,1
# [6,5]
# [4,5]
# [8,7]
print(a[:2,1:4])
# row==>0,1  column=1,2,3
# arange with reshape
a=np.arange(1,26).reshape([5,5])
print(a)
print("*"*100)
# 3D  5*6 matrix
a=np.arange(1,31).reshape([1,5,6])
print(a)
# sort 1D 2D
import numpy as np
a=np.array([4,5,8,1,2,3,4,9,6])
b=np.sort(a)
print(b)
# ascending order,if not specified
b=np.sort(a)
# descending order
c=b[::-1]
print(c)
# or
b=np.sort(a)[::-1]
print(b)
# SPLIT
import numpy as np
a=np.array([4,5,6,7,10,4,2,11,12,8,8,6,6])
b=np.array_split(a,3)
print(b)
import numpy as np
a=np.array([4,5,8,0,2,3,4,12,6])
# # ======sum======
b=np.sum(a)
print(b)
print('*'*100)
# # ======max======
m=np.max(a)
print(m)
print('*'*100)
# # ======min======
mini=np.min(a)
print(mini)
print('*'*100)

z=np.array([[[3,4,5,0],[5,10,7,4],[4,3,2,8],[7,2,3,4]]])

# # ======sum======
b=np.sum(z)
print(b)
# # sum=sum of elements
# # ==========max============
# # max of elements
m=np.max(z)
print(m)
# # =========min======
# # min of elements
minimum=np.min(z)
print(minimum)
# # ==========imp concept===========
#
# # sum of columns,sum of rows
# # axis==>to collect rows and column
# # axis=0:to collect column_sum
# # axis=1:to collect rows
#
z=np.array([[3,4,5,0],[5,10,7,4],[4,3,2,8],[7,2,3,4]])
s=np.sum(z,axis=1)
print(s)
# ============max==============
# row
d=np.max(z,axis=1)
print(d)
# column
d=np.max(z,axis=0)
print(d)
# ======min====
d=np.min(z,axis=1)
print(d)
# column
d=np.min(z,axis=0)
print(d)
import numpy as np
a=np.array([4,5,6,7,10,4,2,11,12,8])
# 'where' returns index of found value
# condition can be <,> = or any other relational operators
b=np.where(a>6)
print(b)
# Ans:(array([3, 4, 7, 8, 9]),)
# (array([3, 4, 7, 8, 9]),)
# (array([3, 4, 7, 8, 9]),)
# =======2D=============
a=np.array([[3,4,5,0],[5,10,7,4],[4,3,2,8],[7,2,3,4]])
b=np.where(a>6)
print(b)
# Ans:(array([1, 1, 2, 3]), array([1, 2, 3, 0]))
# ist array  is row & 2nd array is column
# (1,1)(1,2) (2,3) (3,0) are the index values
# all elements are zero==zeromatrix
# [0,0,0]
# [0,0,0]
import numpy as np
a=np.zeros([3,3])
# [3,3]==>is the order
print(a)
a=np.zeros([3,3],dtype=int)
print(a)
# default datatype: float
# 1D with order=8
import numpy as np
a=np.zeros([8],dtype=int)
print(a)

# 2D with order (4,5)
a=np.zeros([4,5],dtype=int)
print(a)

# order=(5,5) 3D
import numpy as np

a = np.zeros([2,5,5], dtype=int)
print(a)