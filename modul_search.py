
def linear_search(data, target):
    for i in range(len(data)):
        if data[i].lower() == target:     
            return i
    return -1                        

def binary_search(data, target):
    data_sorted = sorted(data)  
    low = 0
    high = len(data_sorted) - 1

    while low <= high:
        mid = (low + high) // 2
        if data_sorted[mid].lower() == target:   
            return mid                       
        elif data_sorted[mid].lower() < target.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1                             
