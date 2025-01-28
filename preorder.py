class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

# Preorder tree traversal
def preorder(root):
    if root is None:
        return
    print(root.data, end=", ")
    preorder(root.leftchild)
    preorder(root.rightchild)

# Insertion of new values into the tree (no duplicates)
def insert(root, newvalue):
    if root is None:
        return BinaryTreeNode(newvalue)
    if newvalue < root.data:
        root.leftchild = insert(root.leftchild, newvalue)
    elif newvalue > root.data:  # Ensure no duplicates
        root.rightchild = insert(root.rightchild, newvalue)
    return root

# Helper function to print values with line breaks after each traversal
def print_tree(root):
    print("Preorder traversal: ", end="")
    preorder(root)
    print()  # New line after traversal

# Main function to create the tree and test the print
root = BinaryTreeNode(20)
root = insert(root, 52)
root = insert(root, 10)
root = insert(root, 22)
root = insert(root, 12)
root = insert(root, 32)
root = insert(root, 24)
root = insert(root, 92)
root = insert(root, 2)
root = insert(root, 82)

# Print the values in preorder
print_tree(root)
