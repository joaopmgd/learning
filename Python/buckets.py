def area_of_water(array):
    max_water = array[:]
    
    max_value = 0
    for i in range(len(array)):
        if array[i] > max_value:
            max_value = array[i]
        max_water[i] = max(max_value, array[i])

    max_value = 0
    for i in reversed(range(len(array))):
        if array[i] > max_value:
            max_value = array[i]
        max_water[i] = min(max_value, max_water[i]) 

    water_area = 0
    for i in range(len(array)):
        water_area += max_water[i] - array[i]

    return water_area

if __name__ == '__main__':
    array = [[10, 2, 4, 0, 3, 1, 2, 5],
            [1, 2, 2, 4, 3, 2, 1, 0],
            [4, 0, 3, 1, 2]]
    for hist in array:
        print(area_of_water(hist))


    # |
    # |
    # |
    # |
    # |___________________
    # | *  *  *  *  *  *  |
    # | *  |  *  *  *  *  |
    # | *  |  *  |  *  *  |
    # | |  |  *  |  *  |  |
    # | |  |  *  |  |  |  |