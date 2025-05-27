class Solution( object )  : 
    def intersec( self , nums1 , nums2 )  : 
        counts = Counter(nums1) 
        result = []

        for num in nums2 : 
            if counts[num] > 0 :
                result.append(num)
                counts[num] -= 1
            
        return result
