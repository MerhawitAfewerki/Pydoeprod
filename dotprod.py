import matplotlib.pyplot as plt
import numpy as np
mata = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matb = np.array([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
  
matrix_product = np.matmul(mata, matb)
print("Matrix Product is ")
print(matrix_product)
print()