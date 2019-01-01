class BinearySearch:
    def search(self, arr, target):
        start = 0
        end = len(arr) - 1
        res = self.helper(arr, start, end, target)
        if res is None:
            print "Target not found"
        else:
            print "Target found at index: ", res

    def helper(self, arr, start, end, target):
        while(start <= end):
            mid = (start + end)/2
            elem = arr[mid]
            if elem == target:
                return mid
            elif elem > target:
                end = mid
            else:
                start = mid + 1
        return



test = BinearySearch()
arr = [1,2,3,4,5,6,7,8,9]
test.search(arr, 6)
