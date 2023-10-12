import numpy as np

x = np.array([[1,2],[3,4]], dtype =np.float64)
y = np.array([[6,9],[4,4]],dtype =np.float64)
print("x=",x)
print("y=",y)
print("element wise assition :",np.add(x,x))
print("element wise subtraction :",np.subtract(x,y))
print("element wise multiplication :",np.multiply(x,y))
print("element wise square root:",np.sqrt(x))
print("matrix multiplication :",np.dot(x,y))
print("sum of elements of matrix x:",np.sum(x))
print("sum of elements in each column of matrix y :",np.sum(y,axis=0))
print("sum of elements in each row of matrix y :",np.sum(y,axis=1))
print("Transpose of x :,x.T")

