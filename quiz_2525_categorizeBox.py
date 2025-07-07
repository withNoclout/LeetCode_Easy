class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        is_bulky = length >= 10**4 or width >= 10**4 or height >= 10**4 or (length * width * height) >= 10**9
        is_heavy = mass >= 100
        
        if is_bulky and is_heavy:
            return "Both"
        elif is_bulky:
            return "Bulky"
        elif is_heavy:
            return "Heavy"
        else:
            return "Neither"
