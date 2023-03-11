class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, data):
        self.next = data


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if not cur_node:
            self.head = new_node
            return
        while cur_node.get_next():
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def println(self):
        list_node = []
        cur_node = self.head
        while cur_node:
            list_node.append(cur_node.get_data())
            cur_node = cur_node.get_next()
        return list_node

    def reverse(self):
        cur_node = self.head
        prev_node = None
        next_node = None

        while cur_node:
            next_node = cur_node.get_next()
            cur_node.set_next(prev_node)
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def __len__(self):
        count = 0
        cur_node = self.head
        while cur_node:
            count += 1
            cur_node = cur_node.get_next()
        return count

    def __iter__(self):
        self.node = self.head
        return self

    def __next__(self):
        if not self.node:
            raise StopIteration
        data = self.node.get_data()
        self.node = self.node.get_next()
        return data
