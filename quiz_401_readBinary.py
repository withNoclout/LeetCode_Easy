class Solution(object):
    def readBinaryWatch(self, turnedOn):
        """
        :type turnedOn: int
        :rtype: List[str]
        """
        result = []
        for h in range(12):        # Hours: 0 - 11
            for m in range(60):    # Minutes: 0 - 59
                # Count the total number of 1s in hour and minute
                if (bin(h) + bin(m)).count('1') == turnedOn:
                    result.append("%d:%02d" % (h, m))
        return result

