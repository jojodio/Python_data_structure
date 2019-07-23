class LNode:
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_

    #返回节点的数据
    def get_data(self):
        return self.data

    #更新节点的数据
    def set_data(self, new_data):
        self.data = new_data

    #返回后继节点
    def get_next(self):
        return self.next

    #变更后继节点
    def set_next(self, new_next):
        self.next = new_next

class Llist:
    def __init__(self):
        self._head = None

    #delete the first element and return the detele element
    def pop(self):
        if self._head is None:
            print('the list is empty')
        else :
            e = self._head.elem
            self._head = self._head.next
        return e

    #judge a list is empty or not
    def is_empty(self):
            if self._head == None:
                print('The list is empty')
            else:
                print('the list is not empty')

    #insert a element in the first
    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    #insert a element in the last
    def append(self, elem):
        if self._head == None:
            self._head = elem
        else:
            p = self._head
            while p.next is not None:
                p = p.next
            p.next = elem
        return

    
