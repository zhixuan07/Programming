import queue

class TreeNode:
    def __init__(self,data):
        self.item = data
        self.leftChild=None
        self.rightChild =None


class BST:
    def __init__(self):
        self.__root =None
        self.__numOfItem = 0

    def size(self):
        return self.__numOfItem

    def search(self,data):
       if self.__root == None :
          return False
       curr = self.__root
       while curr!=data :
          if data < curr.item and curr.leftChild != None :
             curr =  curr.leftChild
       #to be completed

    def insert(self,data):
        newNode = TreeNode(data) #create new Node
        if self.__root == None:   #if BST is empty
            self.__root = newNode
        else:
            curr = self.__root
            par = None

            while curr!=None:    #traversal until leaf 
                par = curr
                if data < curr.item :
                    curr = curr.leftChild
                elif data > curr.item:
                    curr = curr.rightChild
                else:
                    return False   #no allow duplicate value insert

            if data < par.item: 
                par.leftChild = newNode  #insert as left child
            else:
                par.rightChild = newNode #insert as right child
        self.__numOfItem += 1
        return True

    def __remove(self,data):
        pass
        # implementation required 
        

    def displayAll(self):
       # self.__inOrder(self.__root)
       self.__levelOrder();

    def __inOrder(self, TreeNode):
        if TreeNode == None:
            return
        self.__inOrder(TreeNode.leftChild)
        print(TreeNode.item)
        self.__inOrder(TreeNode.rightChild)

    def __levelOrder(self):

        if (self.__root == None):
            return

        q = queue.Queue(self.__numOfItem)
        q.put(self.__root)

        while (not q.empty()) :
            curr = q.get()
            print (curr.item , " ")

            if (curr.leftChild):
                q.put(curr.leftChild)

            if (curr.rightChild):
                q.put(curr.rightChild)


myBst = BST()
myBst.insert(40)
myBst.insert(10)
myBst.insert(15)
myBst.insert(50)
myBst.displayAll()



