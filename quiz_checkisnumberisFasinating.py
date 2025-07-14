def isFascinating(n):
    # Concatenate n, 2*n, and 3*n
    s = str(n) + str(2 * n) + str(3 * n)
    
    # Check if length is 9 and no zeros
    if len(s) != 9 or '0' in s:
        return False
    
    # Check if all digits from 1 to 9 appear exactly once
    return len(set(s)) == 9
