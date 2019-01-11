class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right, self.left = None, None

class BST:
    def __init__(self, root):
        self.root = root
        self.count = 0

    def insert(self, val):
        valNode = TreeNode(val)
        self._insert(valNode, self.root)
           
    def _insert(self, valNode, root):
        if valNode.val >= root.val:
            if root.right is not None:
                self._insert(valNode, root.right)
            else:
                root.right = valNode
        if valNode.val < root.val:
            if root.left is not None:
                self._insert(valNode, root.left)
            else:
                root.left = valNode

    def get_height(self, node):
        return self._get_height(node)

    def _get_height(self, current):
        if current is None:
            return 0 
        leftP = self._get_height(current.left)
        rightP = self._get_height(current.right)
        lc = 0
        rc = 0
        if current.left is not None:
            lc = leftP + 1
        if current.right is not None:
            rc = rightP + 1
        return max(lc, rc)
        


    def get_min(self):
        return self._get_min(self.root)
        
    def _get_min(self, root):
        if root.left is not None:
            return self._get_min(root.left)
        else:
            return root.val

    def get_max(self):
        return self._get_max(self.root)
    
    def _get_max(self, root):
        if root.right is not None:
            return self._get_max(root.right)
        else:   
            return root.val
    
    def is_in_tree(self, val):
        return self._is_in_tree(val, self.root) 

    def _is_in_tree(self, val, root):
        if root is None:
            return False
        if val == root.val:
            return True
        elif val < root.val:
            return self._is_in_tree(val, root.left)
        elif val > root.val:
            return self._is_in_tree(val, root.right)

    def get_node_count(self):
        self._get_node_count(self.root)
        return self.count

    def _get_node_count(self, root):
        if root is None:
            return
        self._get_node_count(root.left)
        self.count += 1
        self._get_node_count(root.right)
        
        
    def print_values(self, root):
        if root is None:
            return
        self.print_values(root.left)
        print root.val
        self.print_values(root.right)
       
    def is_binary_search_tree(self, node):
        return self._is_binary_search_tree(node, float('-inf'), float('inf'))

    def _is_binary_search_tree(self, root, min, max):
        if root is None:
            return True
        if (root.val >= min and root.val < max and self._is_binary_search_tree(root.right, root.val, max) and self._is_binary_search_tree(root.left, min, root.val)):
            return True
        else:
            return False

    def delete_value(self, val):
        self.root = self._delete_value(self.root, val)
        return self.root

    def _delete_value(self, root, val):
        if root is None:
            return root
        if val < root.val:
            root.left = self._delete_value(root.left, val)
        elif val > root.val:
            root.right = self._delete_value(root.right, val)
        else:
        # if the node to be deleted is leaf
            if root.left is None and root.right is None:
                return None
        # if the node has one child
            elif root.left is not None and root.right is None:
                return root.left
            elif root.right is not None and root.left is None:
                return root.right
        # if the node has two children
            elif root.right is not None and root.left is not None:
                rightTreeMin = self._get_min(root.right)
                root.val = rightTreeMin
                root.right = self._delete_value(root.right, rightTreeMin)
                return root
        return root

    def get_successor(self, val):
        current = self.find(self.root, val)
        if current is None: 
            return None
        if current.right is not None:
            return self._get_min(current.right)
        else:
            successor = None
            ancestor = self.root
            while(ancestor != current):
                if(current.val < ancestor.val):
                    successor = ancestor
                    ancestor = ancestor.left
                else:
                    ancestor = current.right
            return successor.val
            

    def find(self, root, val):
        if root is None:
            return root
        if val < root.val:
            return self.find(root.left, val)
        elif val > root.val:
            return self.find(root.right, val)
        else:
            return root
                
        
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node3.left = node2
node2.left = node1
node3.right = node5
node5.left = node4
node5.right = node6
test = BST(node3)
print "print the tree from min to max: " 
test.print_values(node3)
print "node count: ", test.get_node_count()
node7 = TreeNode(7)
test.insert(7)
print "after inserting 7: "
test.print_values(node3)
print "after inserting 3: "
test.insert(3)
test.print_values(node3)
print "is 1 in the tree?"
print test.is_in_tree(1)
print "is 10 in the tree?"
print test.is_in_tree(10)
print "the min value is: ", test.get_min()
print "the max value is: ", test.get_max()
print "the height of node 3: ", test.get_height(node3)
print "the height of node 4: ", test.get_height(node4)
print "the height of node 1: ", test.get_height(node1)
print "the height of node 7: ", test.get_height(node7)
print "is the tree a binary search tree? ", test.is_binary_search_tree(node3)
print "get the successor of 5: ", test.get_successor(5)
print "get the successor of 2: ", test.get_successor(2)
print "delete value 1: "
new1 = test.delete_value(1)
test.print_values(new1)
print "delete value 4: "
new2 = test.delete_value(4)
test.print_values(new2)
print "delete value 5: "
new3 = test.delete_value(5)
test.print_values(new3)
