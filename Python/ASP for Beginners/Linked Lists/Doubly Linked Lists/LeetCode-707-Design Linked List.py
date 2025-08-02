# https://leetcode.com/problems/design-linked-list/description/

'''

Questins at the beggining
1) Do we deal with large amount of elements, or can i ask whether the linked list will be big?
I am asking that because we can optimize search time by starting from head or tail of the list.

'''


class Node():
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.val)

class MyLinkedList(object):

    def __init__(self):
        self.tail = None
        self.head = None
        self.cnt = 0

    def __repr__(self):
        curr = self.head
        retstr = ""
        while curr:
            retstr += str(curr.val) + " "
            curr = curr.next
        return retstr

    def getNode(self, index):
        if index < 0 or index > self.cnt - 1:
            return -1

        if index < self.cnt // 2:
            curr = self.head
            counter = 0
            while counter  < index:
                curr = curr.next
                counter += 1
            return curr
        else:
            curr = self.tail
            counter = self.cnt - 1
            while counter > index:
                curr = curr.prev
                counter -= 1
            return curr
            
    def get(self, index):
        retval = self.getNode(index)
        if  retval != -1:
            return retval.val
        else: return retval
        

    def addAtHead(self, val):
        self.cnt += 1
        newNode = Node(val)
        if not self.head:
            self.head = self.tail = newNode
            return

        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        

    def addAtTail(self, val):
        self.cnt += 1
        newNode = Node(val)
        if not self.head:
            self.head = self.tail = newNode
            return

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        
    # 2<->3<->4
    def addAtIndex(self, index, val):
        if index < 0 or index > self.cnt:
            return
        
        if index == self.cnt:
            self.addAtTail(val)
            return

        node = self.getNode(index)
        newNode = Node(val)
        if index != 0:
            print("get if")
            node.prev.next = newNode
        else:
            print("get else")
            self.ead = newNode
    
        newNode.next = node
        newNode.prev = node.prev
        node.prev = newNode

        self.cnt += 1
        
    # None<-0<-1->2<->3->None
    def deleteAtIndex(self, index):
        node = self.getNode(index)
        if node == -1:
            return

        if index != 0:
            node.prev.next = node.next
        else:
            self.head = node.next
        if index != self.cnt - 1:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = node.next = None

        self.cnt -= 1

        

        


# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()

print("#### INSERT 10 ####")
obj.addAtIndex(0, 10)
print(obj)
print(obj.head.val)
print(obj.tail.val)
print("#### INSERT 20 ####")
obj.addAtIndex(0, 20)
print(obj)
print(obj.head.val)
print(obj.tail.val)
print("#### INSERT 30 ####")
obj.addAtIndex(1, 30)
print(obj)
obj.get(0)