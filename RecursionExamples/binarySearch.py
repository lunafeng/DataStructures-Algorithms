class BinarySearch:
    def search(self, inputArr, target):
        inputArr.sort()
        self.inputArr = inputArr
        print self.inputArr
        return self.helper(0, len(inputArr) - 1, target)

    def helper(self, start, end, target):
        if start > end:
            return 
        mid = (start + end)/2
        if self.inputArr[mid] == target:
            return mid
        if self.inputArr[mid] < target:
            start = mid + 1
            return self.helper(start, end, target)
        else:
            end = mid - 1
            return self.helper(start, end, target)


test = BinarySearch()
arr = [5,4,3,7,9,12,34,56]
print test.search(arr, 7)
print test.search(arr, 12)
print test.search(arr, 0)
