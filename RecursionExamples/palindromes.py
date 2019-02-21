class Palindromes:
    def isPalindromes(self, s):
        s = s.replace(" ", "")
        return self.isValid(s)

    def isValid(self, s):
        if s == "" or len(s) == 1:
            return True
        firstC = s[0]
        secondC = s[-1]
        middleS = s[1:-1]
        
        return firstC == secondC and self.isValid(middleS)
        
        

test = Palindromes()
s = "was it a car or a cat i saw"
print test.isPalindromes(s)
