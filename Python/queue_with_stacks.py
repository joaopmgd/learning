class Queue:

    def __init__(self):
        self.enqueue = []
        self.dequeue = []
    
    def add(self, value):
        self.enqueue.append(value)

    def poll(self):
        self.change_stacks()
        return self.dequeue.pop()

    def change_stacks(self):
        if len(self.dequeue) == 0:
            while (len(self.enqueue) > 0):
                self.dequeue.append(self.enqueue.pop())
                
    def peek(self):
        self.change_stacks()
        return self.dequeue[len(self.dequeue)-1]

    def is_empty(self):
        self.change_stacks()
        return len(self.dequeue) == 0

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


