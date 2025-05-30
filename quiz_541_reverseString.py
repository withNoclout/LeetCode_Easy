class Solution( object ) : 
    def reverseStr( self , s , k):
        s = list(s)

        for i in range( 0 , len(s) , 2*k)  : 
            s[i: i+k] = reversed( s[i:i+k])

        return  ''.join(s) 
    

class Solution: 
    def reverseStr(self, s , k):
        s = list(s)  # แปลง string เป็น list เพื่อแก้ไขได้

        for i in range(0, len(s), 2 * k):
            # กลับเฉพาะ k ตัวแรกในช่วง 2k
            s[i:i+k] = reversed(s[i:i+k])

        return ''.join(s)

