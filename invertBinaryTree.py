from treelib import Tree


def invertBinaryTree(root):
    # [1]
    stack = [None, root]
    # 1
    curr = stack.pop()
    while(curr != None):
        # [2] | [2,6]
        if curr.left:
            stack.append(curr.left)
        # [2, 3] | [2,6,7]
        if curr.right:
            stack.append(curr.right)
        # 2 | 6
        left = curr.left
        # 3 | 7
        right = curr.right
        # 3 | 7
        curr.left = right
        # 2 | 6
        curr.right = left
        # 3 | 7 | 6 | 2
        curr = stack.pop()
    
    return root


# A function to do inorder tree traversal
def printInorder(root):
    if root:
        # First recur on left child
        printInorder(root.left)
        # then print the data of node
        print(root.value),
        # now recur on right child
        printInorder(root.right)


class BinaryTree():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def printTree(root):
    itree = Tree()
    stack = [(None, root)]
    while len(stack) > 0:
        node = stack.pop()
        if node[1] is not None:
            print(node[1].value, end="\n---\n")
            itree.create_node(str(node[1].value), str(node[1].value), parent=str(node[0].value) if node[0] is not None else None)
            stack.append((node[1], node[1].left))
            stack.append((node[1], node[1].right))
    print(','.join([itree[node].tag for node in itree.expand_tree(mode=Tree.WIDTH)]))


if __name__ == "__main__":
    root = BinaryTree(1)
    child_1_1 = BinaryTree(2)
    child_1_2 = BinaryTree(3)
    child_2_1 = BinaryTree(4)
    child_2_2 = BinaryTree(5)
    child_2_3 = BinaryTree(6)
    child_2_4 = BinaryTree(7)

    root.left = child_1_1
    root.right = child_1_2

    child_1_1.left = child_2_1
    child_1_1.right = child_2_2

    child_1_2.left = child_2_3
    child_1_2.right = child_2_4

    printInorder(invertBinaryTree(root))

    # tree = Tree()
    # tree.create_node(1, 'root', parent=None)
    # tree.create_node(2, 'child_1_1', parent="root")
    # tree.create_node(3, 'child_1_2', parent="root")
    # tree.create_node(4, 'child_2_1', parent="child_1_1")
    # tree.create_node(5, 'child_2_2', parent="child_1_1")
    # tree.create_node(6, 'child_2_3', parent="child_1_2")
    # tree.create_node(7, 'child_2_4', parent="child_1_2")
    # tree.show()

    # new_root = invertBinaryTree(root)
    # printTree(new_root)