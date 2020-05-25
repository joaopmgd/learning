# Input: {4, 2, -3, 1, 6}
# Output: true
# There is a subarray with zero sum from index 1 to 3.
 
# Input: {4, 2, 0, 1, 6}
# Output: true
# There is a subarray with zero sum from index 2 to 2.
 
# Input: {-3, 2, 3, 1, 6}
# Output: false
# There is no subarray with zero sum.

def hasZeroSum_N(hasZeroSumArray):
    sum_hash = {0: True}
    for position in range(len(hasZeroSumArray)):
        sum_value = sum(hasZeroSumArray[position:])
        if sum_value in sum_hash:
            return True
        else:
            sum_hash[sum_value] = True
    return False
    

def hasZeroSum_N_SQUARED(hasZeroSumArray):
    for position, number in enumerate(hasZeroSumArray):
        sum_value = number
        if sum_value == 0:
            return True
        for newNumber in hasZeroSumArray[position + 1:]:
            sum_value = sum_value + newNumber
            if sum_value == 0:
                return True
    return False

hasZeroSumArray = [
    [-3, 2, 3, 1, 6],
    [4, 2, 0, 1, 6],
    [4, 2, -3, 1, 6]
]
for array_value in hasZeroSumArray:
    print(hasZeroSum_N_SQUARED(array_value))
for array_value in hasZeroSumArray:
    print(hasZeroSum_N(array_value))