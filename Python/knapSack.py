
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
number_of_items = len(values)
max_capacity = 7

# matrix of items x capacity
knapSack_table = [0] * (number_of_items + 1)
for i in range(number_of_items + 1):
    knapSack_table[i] = [0] * (max_capacity + 1)

def create_knapSack_table():
    for item in range(1, number_of_items + 1):
        for capacity in range(1, max_capacity + 1):
            if capacity >= weights[item - 1]:
                knapSack_table[item][capacity] = max(knapSack_table[item - 1][capacity], values[item-1] +  knapSack_table[item - 1][capacity - weights[item-1]])
            else:
                knapSack_table[item][capacity] = knapSack_table[item - 1][capacity]
            
def print_knapSack_table():
    for item_line in knapSack_table:
        print(item_line)

def find_items():
    items = [0] * (number_of_items)
    max_value = knapSack_table[number_of_items][max_capacity]
    print('Total Benefit: ' + str(max_value))

    capacity = max_capacity

    for item in reversed(range(number_of_items+1)):
        if knapSack_table[item][capacity] != 0 and knapSack_table[item][capacity] != knapSack_table[item - 1][capacity]:
            items[item-1] = 1
            capacity = capacity - weights[item-1]

    for item in range(len(items)):
        if items[item] == 1:
            print('Product: ' + str(item + 1) + ' of value: ' + str(values[item]) + ' and weight: ' + str(weights[item]) +' accepted.')

if __name__ == '__main__':
    create_knapSack_table()
    print_knapSack_table()
    find_items()