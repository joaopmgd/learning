import math

##################################
##                              ##
##          QUICK SORT          ##
##                              ##
##################################
def quicksort(array):
    sorted_array = array[:]
    quicksort_recursion(sorted_array, 0, len(array)-1)
    return sorted_array

def quicksort_recursion(sorted_array, left, right):
    if left >= right:
        return
    
    pivot = sorted_array[(left + right) // 2]
    index = partition(sorted_array, left, right, pivot)
    quicksort_recursion(sorted_array, left, index - 1)
    quicksort_recursion(sorted_array, index, right)

def partition(sorted_array, left, right, pivot):
    while (left <= right):

        while sorted_array[left] < pivot:
            left += 1
            
        while sorted_array[right] > pivot:
            right -= 1

        if left <= right:
            sorted_array = swap(sorted_array, left, right)
            left += 1
            right -= 1

    return left

##################################
##                              ##
##          MERGESORT           ##
##                              ##
##################################

def mergesort(array):
    sorted_array = array[:]
    mergesort_recursion(array, sorted_array, 0, len(array)-1)
    return sorted_array

def mergesort_recursion(array, sorted_array, left, right):
    if left >= right:
        return
    
    middle = (left + right) // 2
    mergesort_recursion(array, sorted_array, left, middle)
    mergesort_recursion(array, sorted_array, middle + 1, right)
    merge_halves(array, sorted_array, left, right)

def merge_halves(array, sorted_array, left_start, right_end):
    left_end = (right_end + left_start) // 2
    right_start = left_end + 1
    size = right_end - left_start + 1

    left = left_start
    right = right_start
    index = left_start

    while left <= left_end and right <= right_end:
        if array[left] <= array[right]:
            sorted_array[index] = array[left]
            left += 1
        else:
            sorted_array[index] = array[right]
            right += 1
        index += 1

    while left < left_end + 1:
        sorted_array[index] = array[left]
        index+= 1
        left += 1

    while right < right_end + 1:
        sorted_array[index] = array[right]
        index += 1
        right += 1

    for i in range(len(sorted_array)):
        array[i] = sorted_array[i]



##################################
##                              ##
##          HEAPSORT            ##
##                              ##
##################################

def heapsort(array):
    sorted_array = []
    while len(array) > 0:
        heapfy(array)
        sorted_array.append(heap_pop(array))
    return sorted_array

def heapfy(array):
    index = 0
    while index < len(array):
        lowest_child = get_lowest_child_index(array, index)
        if lowest_child != None and array[index] > array[lowest_child]:
            swap(array, index, lowest_child)
            index = get_parent(index)
        else:
            index += 1

def get_parent(index):
    level = index - 2
    if level < 0:
        level = 0
    parent = math.ceil(level / 2)
    if parent >= 0:
        return parent
    else:
        return index


def get_lowest_child_index(array, index):
    left_child, right_child = None, None
    if len(array) > (index * 2) + 1:
        left_child = (index * 2) + 1
    if len(array) > (index * 2) + 2:
        right_child = (index * 2) + 2
    if left_child == None and right_child == None:
        return None
    if left_child != None and right_child == None:
        return left_child
    if right_child != None and left_child == None:
        return right_child
    if array[left_child] < array[right_child]:
        return left_child
    return right_child

def heap_pop(array):
    swap(array, 0, len(array)-1)
    return array.pop()

def print_heap(array):
    new_line = 0
    line_items = 0
    for item in range(len(array)):
        if new_line == line_items:
            print(array[item])
            if line_items == 0:
                line_items += 2
            else:
                line_items *= 2
            new_line = 1
        else:
            print(str(array[item]) + " ", end='')
            new_line += 1
    print()



##################################
##                              ##
##            UTILS             ##
##                              ##
##################################

def swap(array, left, right):
    temp = array[left]
    array[left] = array[right]
    array[right] = temp
    return array



##################################
##                              ##
##            MAIN              ##
##                              ##
##################################

if __name__ == '__main__':
    array = [6, 3, 2, 1, 5, 9, 7, 8, 15, 12, 10, 4,]
    print('Unsorted : ' + str(array))
    print('Quicksort: ' + str(quicksort(array)))
    print('Mergesort: ' + str(mergesort(array[:])))
    print('Heapsort : ' + str(heapsort(array)))