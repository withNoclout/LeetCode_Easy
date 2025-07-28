class Solution(object):
    def concatHex36(self, n):
        """
        :type n: int
        :rtype: str
        """
        hex_chars = '0123456789abcdef'
        n_square = n * n
        hex_result = ''

        if n_square == 0:
            hex_result = '0' 

        else : 

            while n_square > 0:
                hex_result = hex_chars[n_square % 16] + hex_result
                n_square //= 16
        hexatri_chars = '0123456789abcdef0123456789abcdef0123456789abcdef'
        n_cube = n* n * n 
        hexatri_result = ''

        if n_cube == 0:
            hexatri_result = '0'
        else : 
            while n_cube > 0:
                hexatri_result = hexatri_chars[n_cube % 36] + hexatri_result
                n_cube //= 36
        return hex_result + hexatri_result
