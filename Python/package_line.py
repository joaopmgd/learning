import time

def check_destination(stream, k):
    value = next(stream, None)
    position = 0
    values_in_line = dict()
    queue = []
    first_element = -1
    while value != None:

        position = position % k

        if len(queue) == k:
            first_element = queue.pop(0)

        if first_element in values_in_line and values_in_line[first_element] == position:
            del values_in_line[first_element]

        if value in values_in_line:
            print('SAME PLACE', value)

        values_in_line[value] = position
        queue.append(value)

        position += 1
        value = next(stream, None)
        # time.sleep(5)


if __name__ == '__main__':
    stream = iter('1224524511111')
    k = 4
    check_destination(stream, k)