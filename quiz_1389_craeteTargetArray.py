class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = [] 
        for num , idx in zip( nums , index ) :
            target.insert( idx , num )

        return target
