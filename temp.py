import numpy as np
array = np.array([1,22,3,5,7,444,3,8,36,35,767,4,6])
array = np.sort(array)
k = int(input("Enter No of cases "))
j = 0
lent = len(array)-1
for i in range(k):
    print(array[lent-j])
    j = j+1
