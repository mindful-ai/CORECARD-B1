class treenode(object):

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class binarytree(object):

    def __init__(self):
        self.root = None

    def sampletree(self):
        t1 = treenode(10)
        t2 = treenode(20)
        t3 = treenode(30)
        t4 = treenode(40)
        t5 = treenode(50)
        t6 = treenode(60)
        t7 = treenode(70)
        t1.left = t2
        t1.right = t3
        t2.left = t4
        t2.right = t5
        t3.left = t6
        t3.right = t7
        self.root = t1

    # in-order traversing
    def traverse1(self, root):
        if(root):
            self.traverse1(root.left)
            print(root.data)
            self.traverse1(root.right)

    # pre-order traversing
    def traverse2(self, root):
        if(root):
            print(root.data)
            self.traverse2(root.left)
            self.traverse2(root.right)

    # post-order traversing
    def traverse3(self, root):
        if(root):
            self.traverse3(root.left)
            self.traverse3(root.right)
            print(root.data)

    # Non-recursive traversing of the tree
    def traverse(self, root):
        pass

    # algorithm to build a tree using a series of data objects
    def buildtree(self, data):
        pass




# -------------------------------------------------

t = binarytree()
t.sampletree()
print(t.root.data)
print(t.root.left.data, t.root.right.data)

print("\nTraversing the tree... \n")
t.traverse1(t.root)

print("\nTraversing the tree... \n")
t.traverse2(t.root)

print("\nTraversing the tree... \n")
t.traverse3(t.root)