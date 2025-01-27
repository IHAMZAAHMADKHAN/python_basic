class binaryTreeNode : 
     def __init__(self , data):
          self.data=data
          self.leftchild=None
          self.rightchild=None

# preorder travasing 

def preorder(root):
    if root is None:
     return
    print(root.data , end=",")
    preorder(root.leftchild)
    preorder(root.rightchild)


#node insertion 

def insert(root, newvalue):
    if root is None :
        root=binaryTreeNode(newvalue) 
        return
    if newvalue<root.data:
        root.leftchild=insert(root.ledtchild , newvalue) 
    else : 
        root.rightchild=insert(root.rightchild , newvalue)
    return root



root=binaryTreeNode(5)
root.leftchild=binaryTreeNode(2)
root.rightchild=binaryTreeNode(10)

preorder(root)