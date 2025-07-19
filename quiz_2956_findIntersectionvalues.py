class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1 ) 
        set2 = set(nums2) 

        answer1 = 0 
        answer2 = 0

        for num in nums1 :
            if num in set2 : 
                answer1 +=  1 

        for num in nums2 : 
            if num in set1 : 
                answer2 +=  1   

        return [answer1, answer2]
