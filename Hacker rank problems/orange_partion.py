def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def make_partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            swap(arr, i, j)
    swap(arr, i + 1, right)
    return i + 1  # Returning pivot index

# Example usage:
arr = [4, 3, 7, 2, 5]
pivot_index = make_partition(arr, 0, len(arr) - 1)
print("Partitioned Array:", arr)
print("Pivot Index:", pivot_index)
