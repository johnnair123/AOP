import numpy as np
a1=np.array([[1,2,3],[3,4,5],[5,6,7]])
a2=np.array([[7,8,9],[2,4,3],[4,6,2]])
print("Addition")
print(np.add(a1,a2))
print("Subtraction")
print(np.subtract(a1,a2))
print("Multiplication")
print(np.multiply(a1,a2))
print("Division")
print(np.divide(a1,a2))
print("Transpose a1")
print(a1.T)
print("transpose a2")
print(a2.T)
print("sum of diagonals")
print(sum(np.diag(a1)))
print("sum of diagonals")
print(sum(np.diag(a2)))

