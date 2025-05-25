class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        result = []
        if not nums:
            return result

        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                # end of range
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    newt  = str(start)+"->"+str(nums[i-1])
                    result.append(newt)
                start = nums[i]  # start new range

        # Handle the last range
        if start == nums[-1]:
            result.append(str(start))
        else:
            newt2 = str(start)+"->"+str(nums[-1])
            result.append(newt2)

        return result
