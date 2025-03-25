# 2. Reshape a 1D Array into a 2D Matrix 
#  A company's quarterly sales data is stored in a 1D NumPy array: [1000, 1200, 1500, 
# 1800, 2000, 2100, 2500, 2700]. Convert it into a 2D array with 4 rows and 2 columns 
# representing sales per quarter.
import numpy as np
 
array = np.array([1000, 1200, 1500, 1800, 2000, 2100, 2500, 2700])
arr = array.reshape(4,2)
print(arr)