class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


# class Solution(object):
#     def addBinary(self, a, b):
#         """
#         :type a: str
#         :type b: str
#         :rtype: str
#         """
#         return bin(int(a, 2) + int(b, 2))[2:]
    


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        carry = 0

        # Make both strings the same length by padding with zeros
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # Perform binary addition from right to left
        for i in range(max_len - 1, -1, -1):
            bit_sum = int(a[i]) + int(b[i]) + carry
            result.append(str(bit_sum % 2))  # Append the current bit (0 or 1)
            carry = bit_sum // 2  # Update the carry (0 or 1)

        # If there's a carry left, add it to the result
        if carry:
            result.append('1')

        # Reverse the result and join it into a string
        return ''.join(result[::-1])
    
    
