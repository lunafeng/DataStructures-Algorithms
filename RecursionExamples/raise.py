class Raise:
    def pow(self, base, n):
        if n == 0:
            return 1

        if n%2 == 0:
            return self.pow(base**2, n/2)

        else:
            return base * self.pow(base**2, n/2)


test = Raise()
print test.pow(2, 0)
print test.pow(2, 1)
print test.pow(2, 2)
print test.pow(2, 3)
print test.pow(2, 5)
