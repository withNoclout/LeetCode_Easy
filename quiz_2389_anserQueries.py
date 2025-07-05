class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        nums.sort()

        prefix_sum = [0]
        for num in nums :
            prefix_sum.append( prefix_sum[-1] + num ) 

        answer = []
        for query in queries :
            left , right = 0 , len(prefix_sum ) - 1 
            while left <= right :
                mid = ( left + right ) // 2 
                if prefix_sum[mid ] <= query :
                    left = mid + 1 
                else : 
                    right = mid - 1 
            answer.append(right )

        return answer 
