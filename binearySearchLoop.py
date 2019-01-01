class BinearySearch:
    def search(self, arr, target):
        start = 0
        end = len(arr) - 1
        return self.helper(arr, start, end, target)

    def helper(self, arr, start, end, target):
        while(start <= end):
            mid = (start + end)/2
            elem = arr[mid]
            if elem == target:
                return "Found target at index: ", mid
            elif elem > target:
                end = mid
                self.helper(arr, start, end, target)
            else:
                start = mid + 1
                self.helper(arr, start, end, target)
        return "Target not found"



test = BinearySearch()
arr = [1,2,3,4,5,6,7,8,9]
print test.search(arr, 1)
