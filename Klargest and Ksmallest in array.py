import numpy as np

def Klargest(array, k, j=0):
    lent = len(array)-1
    for i in range(k):
        print(array[lent-j])
        j = j+1
    return "\n"

def Ksmallest(array, k):
    for i in range(k):
        print(array[i])
    return "\n"
    
array = np.array([1,22,3,5,7,444,3,8,36,35,77,4,6])
array = np.sort(array)
k = int(input("Enter No of cases "))
print(Klargest(array, k))
print(Ksmallest(array, k))


