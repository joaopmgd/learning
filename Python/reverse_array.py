def swap_array_elements(pos1, pos2, array):
    temp = array[pos1]
    array[pos1] = array[pos2]
    array[pos2] = temp

def reverse_array(array):
    i = 0
    j = len(array) - 1
    while (i <= j):
        swap_array_elements(i,j,array)
        i += 1
        j -= 1
    return array

if __name__ == '__main__':
    array = [1,2,3,4,5,6,7,8,9]
    print(reverse_array(array))