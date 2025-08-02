class Node:
    def __init__(self, key: int, value: int):
        self.left = None
        self.right = None
        self.val = value
        self.key = key

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        
        def insertHelper(root):
            if not root:
                return Node(key, val)

            if root.key > key:
                root.left = insertHelper(root.left)
            elif root.key < key:
                root.right = insertHelper(root.right)
            else:
                root.val = val

            return root

        self.root = insertHelper(self.root)
        


    def get(self, key: int) -> int:

        def getHelper(root):
            if not root:
                return -1

            if root.key > key:
                return getHelper(root.left)
            if root.key < key:
                return getHelper(root.right)
            if root.key == key:
                return root.val

        return getHelper(self.root)
            


    def getMin(self) -> int:
        minNode = self.root

        while minNode and minNode.left:
            minNode = minNode.left

        return minNode.val if minNode else -1


    def getMax(self) -> int:
        maxNode = self.root

        while maxNode and maxNode.right:
            maxNode = maxNode.right

        return maxNode.val if maxNode else -1

    def remove(self, key: int) -> None:

        

        def minHelper(root):
            while root.right:
                root = root.right
            return root

        def removeHelper(curr: Node, key: int) -> Node:

            if not curr:
                return None
            
            if curr.key > key:
                print("left")
                curr.left = removeHelper(curr.left, key)
            elif curr.key < key:
                print("right")
                curr.right = removeHelper(curr.right, key)
            else:
                print("found")
                if not curr.left:
                    print("found left")
                    return curr.right
                if not curr.right:
                    print("found right")
                    return curr.left

                minNode = minHelper(curr.left)

                curr.key = minNode.key
                curr.val = minNode.val

                curr.left = removeHelper(curr.left, minNode.key)
            return curr

        self.root = removeHelper(self.root, key)
        
                
    def getInorderKeys(self) -> List[int]:

        stack = []
        curr = self.root
        outputList = []
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                outputList.append(curr.key)
                curr = curr.right

        return outputList



