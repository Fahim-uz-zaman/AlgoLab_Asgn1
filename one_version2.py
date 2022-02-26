import numpy as np
import sys

original_stdout = sys.stdout # Saving a reference to the original standard output

with open('uniform_data_set.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    for i in range(2**19):
        print(np.random.uniform(0, 1))

with open('normal_data_set.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    for i in range(2**19):
        print(np.random.normal(0.0, 1.0))

    

""" At this point we have the data sets. Now we'll be testing merge sort and
     quick sort with the data"""

#2.A: Testing merge sort with the data:

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
 
 
arr = []
with open('uniform_data_set.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        arr.append(float(line))

n = len(arr)

mergeSort(arr, 0, n-1)

with open('sorted_uniform_data_set.txt', 'w') as f:
    sys.stdout = f
    for element in arr:
        print(element)

sys.stdout = original_stdout # Reset the standard output to its original value

print("Merge sort was applied to the data set.")
print("Sorted data stored in sorted_uniform_data_set.txt.")

# Checking correctness:

arr = []

with open('sorted_uniform_data_set.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        arr.append(float(line))

n = len(arr)

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        print('Merge sort didn\'t work')
        quit()

print('Merge sort worked (Verified)')
