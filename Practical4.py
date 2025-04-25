def accept_array():
    arr = []
    n = int(input("Enter the number of elements in the array: "))
    for i in range(n):
        arr.append(int(input(f"Enter element {i+1}: ")))
    return arr

def display_array(arr):
    n = len(arr)
    if n == 0:
        print("Array is empty")
        return
    print("Array elements:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j           
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        n = len(arr)
