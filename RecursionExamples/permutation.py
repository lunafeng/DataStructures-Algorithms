class Permutation:
    def permute(self, str):
        self.res = []
        self.helper("", str)
        return self.res

    def helper(self, sofar, rest):
        if rest == "":
            print sofar
            return sofar

        for idx, c in enumerate(rest):
            next = sofar + c
            remain = rest[:idx] + rest[idx+1:]
            self.helper(next, remain)


test = Permutation()
print test.permute("abcd")
