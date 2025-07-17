import numpy as np
import scipy

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array) # Average
median = np.median(array) # mid value in the list
mode   = stats.mode(array) # most most occuring element in the list

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode Occurances = ', mode.count)
print(f'Mode Count = ', len(mode.count))