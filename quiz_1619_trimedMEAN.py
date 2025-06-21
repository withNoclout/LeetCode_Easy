class Solution(object):
    def trimMean(self , arr):
        n = len(arr)
        remove_count = n // 20  # 5% of elements
        arr.sort()
        trimmed = arr[remove_count:n-remove_count]
        return sum(trimmed) / len(trimmed)
    
arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]

solution = Solution()
print(solution.trimMean(arr))  # Output: 4.777777777777778
