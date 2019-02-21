class BinearySearch:
    def search(self, arr, target):
        self.LRange = 0
        self.RRange = 0
        start = 0
        end = len(arr) - 1
        res = self.helper(arr, start, end, target)
        print "The target should be between ", str(arr[self.LRange]) + " and " + str(arr[self.RRange])

    def helper(self, arr, start, end, target):
        if start >= end:
            return
        mid = (start + end)/2
        elem = arr[mid]
        self.LRange = mid
        self.RRange = mid + 1
        if elem == target:
            return mid
        elif elem > target:
            end = mid
            return self.helper(arr, start, end, target)
        else:
            start = mid + 1
            return self.helper(arr, start, end, target)

test = BinearySearch()
arr = [1,3,4,5,7,9]
test.search(arr, 2)
