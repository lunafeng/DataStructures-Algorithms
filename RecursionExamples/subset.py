class Subset:
    def getSubset(self, str):
        self.res = []
        self.helper("", str)
        return self.res

    def helper(self, sofar, rest):
        if rest == "":
            self.res.append(sofar)
            return 


        self.helper(sofar + rest[0], rest[1:])
        self.helper(sofar, rest[1:])


test = Subset()
print test.getSubset("abc")
