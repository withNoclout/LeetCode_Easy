class Solution(object):
    def countValidSelections(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len( nums ) 
        valid_count = 0 

        def simulate( start , direction )  : 
            curr =  start 
            dir = direction 
            visited = set()
            nums_copy = nums.copy()

            while 0 <= curr < n : 
                if ( curr , dir ) in visited : 
                    return False 
                visited.add(( curr , dir ))  

                if nums_copy[curr] == 0 :
                    curr += dir 
                else : 
                    nums_copy[curr]  -= 1 
                    dir = -dir 
                    curr += dir 

            return all( x ==  0 for x in nums_copy ) 
        
        for i in range(n)  : 
            if nums[i] == 0 :
                if simulate( i , -1 ) :
                    valid_count += 1 
                if simulate( i , 1  ) :
                    valud_count += 1 

        return valid_count 
    



# ========================


class Solution : 
    def zeroFilledSubArray( self , nums)   :
        n = len(nums ) 
        result = 0 

        for i in range(n)  : 
            if nums[i] == 0 :
                left = i 
                right = i  

                while left - 1 >= 0 and nums[left - 1 ] > 0 :
                    left -= 1 
                while right + 1 <  n and nums[right + 1 ]  > 0 : 
                    right += 1 

                result += 1 

        return result 
    


# ===================


class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        def valid(idx, dist):
            temp = nums[:]
            while 0 <= idx < n:
                if temp[idx] == 0:
                    idx += dist
                else:
                    temp[idx] -= 1
                    dist = -dist
                    idx += dist
            return all(x == 0 for x in temp)
        
        n = len(nums)
        cnt = 0
        for i, x in enumerate(nums):
            if x == 0:
                if valid(i, 1):
                    cnt += 1
                if valid(i, -1):
                    cnt += 1
        return cnt
    
    
