class Queue:

    def __init__(self):
        self.stack = []

    def add(self, value):
        self.stack.append(value)

    def poll(self):
        return self.poll_recursive(self.stack)

    def poll_recursive(self, stack):
        number = stack.pop()
        if len(stack) == 0:
            return number
        first = self.poll_recursive(stack)
        self.stack.append(number)
        return first
                
    def peek(self):
        return self.peek_recursive(self.stack)

    def peek_recursive(self, stack):
        if len(stack) == 1:
            return stack.pop()
        
        return self.peek_recursive(stack[:-1])

    def is_empty(self):
        return len(self.stack) == 0

if __name__ == '__main__':
    numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
    queue = Queue()

    for number in numbers:
        queue.add(number)

    print(queue.peek())
    print(queue.peek())
    print(queue.poll())

    print(queue.peek())
    print(queue.poll())

    new_numbers = [14,15,16,17,18,19,20]

    for number in new_numbers:
        queue.add(number)

    while not queue.is_empty():
        print(queue.poll())