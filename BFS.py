from Queue import Queue
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None

class BFS:

    def search(self, root, target):
        q = Queue()
        if root is None:
            return False
        q.put(root)
        while(q.empty() is False):
            current = q.get()
            if current.val == target:
                return True
            if current.left is not None:
                q.put(current.left)
            if current.right is not None:
                q.put(current.right)
        return False

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node6 = TreeNode(6)
node4.left = node2
node4.right = node6
node2.left = node1
node2.right = node3

test = BFS()
print test.search(node4, 1)

