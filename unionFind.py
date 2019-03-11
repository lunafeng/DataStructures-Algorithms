class UnionFind:
    def __init__(self, N):
        # in this example, the id is the number itself before any union
        self.ids = range(N)

    def root(self, i):
        if self.ids[i] == i:
            return i
        self.ids[i] = self.ids[self.ids[i]]
        return self.root(self.ids[i])

    def find(self, p, q):
        rootP = self.root(p)
        rootQ = self.root(q)
        if rootP == rootQ:
            return True
        else:
            return False

    def union(self, p, q):
        rootP = self.root(p)
        rootQ = self.root(q)
        if rootP != rootQ:
            self.ids[rootP] = rootQ

    def printIds(self):
        print self.ids

test = UnionFind(10)
test.printIds()
test.union(0, 1)
test.union(2, 3)
test.union(0, 2)
test.union(4, 8)
test.union(4, 9)
test.union(5, 6)
test.printIds()

print "test 1, 2"
print test.find(1, 2)
print "test 1, 0"
print test.find(1, 0)
print "test 4, 7"
print test.find(4, 7)
