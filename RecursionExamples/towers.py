class Towers:
    def move(self, src, des, n):
        self.helper(src, des, 'C', n)

    def helper(self, src, des, temp, n):
        if n == 0:
            return 
        self.helper(src, temp, des, n - 1)
        print src + "--->" + des
        self.helper(temp, des, src, n - 1)




test = Towers()
test.move('A', 'B', 3)
