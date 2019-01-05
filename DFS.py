from Queue import Queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None

class DFS:
    def search(self, root, target, method):
        self.found = False
        if method == "inorder":
            self.inorder(root, target)
            return self.found
        if method == "preorder":
            self.preorder(root, target)
            return self.found
        if method == "postorder":
            self.postorder(root, target)
            return self.found

    def inorder(self, root, target):
        if root is None:
            return
        self.inorder(root.left, target)
        if root.val == target:
            self.found = True
        self.inorder(root.right, target)

    def postorder(self, root, target):
        if root is None:
            return
        self.postorder(root.left, target)
        self.postorder(root.right, target)
        if root.val == target:
            self.found = True

    def preorder(self, root, target):
        if root is None:
            return
        if root.val == target:
            self.found = True
        self.preorder(root.left, target)
        self.preorder(root.right, target)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node6 = TreeNode(6)
node4.left = node2
node4.right = node6
node2.left = node1
node2.right = node3

test = DFS()
print test.search(node4, 3, "preorder")
