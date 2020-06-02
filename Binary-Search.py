data = [1,3,6,8,10,13,16,19,20,26,29,33,39]
target = 26

#Liner Search (Takes time, not good for efficiency)
def liner_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
        else:
            return False
# Iterative Binary Search (Assuming Array/List is sorted)
def binary_search_ite(data, target):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
           return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False
# Recursive Binary Search ()
def binary_search_rec(data, target, low, high):
    if low > high:
        return False
    else: mid = (low + high) // 2
    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search_rec(data, target, low, mid - 1)
    else:
        return binary_search_rec(data, target, mid +1, high)
    
print(binary_search_ite(data, target))
print(binary_search_rec(data, target, 0, len(data)-1))