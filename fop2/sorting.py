def swap(lyst, i, j):
    """Exchanges the items at positions i and j."""
    temp = lyst[i]
    lyst[i] = lyst[j]
    lyst[j] = temp


def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:      # Do n-1 searches
        minIndex = i              # for the smallest
        j = i + 1
        while j < len(lyst):      # Start a search
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:         # Exchange if needed
            swap(lyst, minIndex, i)
        i += 1


def bubbleSort(lyst):
    n = len(lyst)
    while n > 1:                  # Do n-1 bubbles
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
            i += 1
        n -= 1


def bubbleSortTweak(lyst):
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        if not swapped: return
        n -= 1


def insertionSort(lyst):
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        lyst[j + 1] = itemToInsert
        i += 1


def quicksort(lyst):
    quicksortHelper(lyst, 0, len(lyst)-1)


def quicksortHelper(lyst, left, right):
    if left < right:
        pivotLocation = partition(lyst, left, right)
        quicksortHelper(lyst, left, pivotLocation-1)
        quicksortHelper(lyst, pivotLocation+1, right)


def partition(lyst, left, right):
    # Find the pivot and exchange it with the last item
    middle = (left + right) // 2
    pivot = lyst[middle]
    lyst[middle] = lyst[right]
    lyst[right] = pivot
    # Set boundary point to first position
    boundary = left
    # Move items less than pivot to the left
    for index in range(left, right):
        if lyst[index] < pivot:
            swap(lyst, index, boundary)
            boundary += 1
    # Exchange the pivot item and the boundary item
    swap(lyst, right, boundary)
    return boundary


import random

def main(size=2000, sort=quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size+1))
    print(lyst)
    sort(lyst)
    print(lyst)


if __name__ == '__main__':
    main()
