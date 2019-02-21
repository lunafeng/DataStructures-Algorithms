class ChoseSubset:
    def chose(self, n, k):
        if k == 0 or k == n:
            return 1
        return self.chose(n-1, k-1) + self.chose(n-1, k)


test = ChoseSubset()
print test.chose(4,2)

        
