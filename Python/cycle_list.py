class Node:
    
    def __init__(self, value=None):
        self.value = value
        self.nextval = None

class LinkedList:

    def __init__(self):
        self.headval = None
        self.tailval = None

    def list_print(self):
        printval = self.headval
        while printval is not None:
            print (printval.value)
            printval = printval.nextval

    def add_element(self, value):
        if self.headval is None:
            self.headval = Node(value)
        else:
            current = self.headval
            while current.nextval is not None:
                current = current.nextval
            current.nextval = Node(value)

    def remove_element(self, value):

        if self.headval == None:
            return

        elif self.headval.value == value:
            self.headval = self.headval.nextval

        else:
            current = self.headval

            while current.nextval is not None and current.nextval.value != value:
                current = current.nextval

            if current.nextval is not None and current.nextval.value == value:
                current.nextval = current.nextval.nextval

    def get_node(self, value):
        current = self.headval
        while current is not None:
            if current.value == value:
                return current
            current = current.nextval

    def has_cycle(self):
        slow = self.headval
        fast = self.headval

        while fast is not None and fast.nextval is not None and fast.nextval.nextval is not None:
            fast = fast.nextval.nextval
            if slow == fast:
                return True

            slow = slow.nextval

        return False
        


if __name__ == '__main__':
    list = LinkedList()

    list.add_element(1)
    list.add_element(2)
    list.add_element(3)
    list.add_element(4)
    list.add_element(5)
    list.add_element(6)
    list.add_element(7)
    list.add_element(8)
    list.add_element(9)
    list.add_element(10)
    list.add_element(11)
    list.add_element(12)
    list.add_element(13)
    list.add_element(14)
    list.add_element(15)
    list.add_element(16)

    list.remove_element(2)

    list.list_print()

    list.get_node(16).nextval = list.get_node(3)

    print(list.has_cycle())