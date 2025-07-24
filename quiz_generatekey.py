class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # Convert numbers to 4-digit strings with leading zeros
        s1, s2, s3 = str(num1).zfill(4), str(num2).zfill(4), str(num3).zfill(4)
        # Take minimum digit at each position
        key = ""
        for i in range(4):
            key += min(s1[i], s2[i], s3[i])
        # Convert to integer to remove leading zeros
        return int(key)
