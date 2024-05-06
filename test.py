class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class AS:
    def __init__(self):
        self.head = None

    def make_as(self, *data):
        for i in data:
            node = Node(i)
            if self.head == None:
                self.head = node
            else:
                itr = self.head
                while itr.next:
                    itr = itr.next
                itr.next = node
    def show_as(self):
        itr = self.head
        print("AS--->", end="")
        while itr:
            print(itr.data, end='->')
            itr = itr.next
    def rev_as(self):
        curr = self.head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def sort_as(self):
        pass


obj = AS()
obj.make_as(1,2,3,4,5,6,7,8,9)
obj.show_as()
obj.rev_as()
print("New line")
obj.show_as()

obj.sort_as()