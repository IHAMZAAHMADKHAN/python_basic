class binaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None


def preorder(root):
    if root is None :
        return
    print(root.data, end=",")
    preorder(root.leftchild)
    preorder(root.rightchild)

#inser new node

def insert(root,newvalue):
    if root is None :
        return binaryTreeNode(newvalue)
    if newvalue<root.data:
        root.leftchild=insert(root.leftchild,newvalue)
    elif newvalue>root.data:
        root.rightchild=insert(root.rightchild , newvalue)
    return root

def print_tree(root):
    print("preoder tree : ", end="")
    preorder(root)
    print()


root=binaryTreeNode(80)
root=insert(root, 90)
root=insert(root, 20)
root=insert(root, 70)
root=insert(root, 50)

print_tree(root)