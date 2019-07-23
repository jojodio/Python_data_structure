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


    # delete the last element and return
    def pop_last(self):
        if self._head == None:
            print("the list is empty")
            return
        else:
            p = self._head
            while p.next.next:
                p = p.next
            e = p.next.elem
            p.next = None
            return e

    #the size of list
    def size(self):
        size = 0
        p = self._head
        while p.next:
            size += 1
            p = p.next
        return size

    def find(self, prep):
        if self._head == None:
            print("the list is empty")
        else:
            p = self._head
            while p:
                if prep(p.elem):
                    return p.elem
                else:
                    p = p.next
        return

    # remove a element by index
    def remove(self, i):
        if self.size() <= i:
            print("please input a small i".format(i))
        elif i == 0:
            if self._head.next == None:
                self._head = None
            else:
                self._head = self._head.next
        elif i == (self.size()-1):
            p = self._head
            while p.next.next:
                p = p.next
            p.next = None
        else:
            p = self._head
            index = 0
            while index < (i-1):
                p = p.next
            p.next = p.next.next
        return

    #add a element by index
    def add(self, i, elem):
        if i >= self.size():
            print("please input a small i".format(i))
        elif i == 0:
            self._head = LNode(elem,self._head)
        else:
            index = 0
            p = self._head
            while index < (i-1):
                p = p.next
            p.next.next = p.next
            p.next = elem
        return

    


