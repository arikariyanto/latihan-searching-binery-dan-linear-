# modul_search.py

# Linear Search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i].lower() == target:     # isian kosong 1
            return i
    return -1                         # isian kosong 2


# Binary Search
def binary_search(data, target):
    data_sorted = sorted(data)  # pastikan data terurut
    low = 0
    high = len(data_sorted) - 1

    while low <= high:
        mid = (low + high) // 2
        if data_sorted[mid].lower() == target:   # isian kosong 3
            return mid                        # isian kosong 4
        elif data_sorted[mid].lower() < target.lower():
            low = mid + 1
        else:
            high = mid - 1
    return -1                              # isian kosong 5
