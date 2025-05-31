class Solution:
    def checkRecord(self, s: str) -> bool:
        # เช็คว่ามี 'A' น้อยกว่า 2 และไม่มี 'LLL'
        return s.count('A') < 2 and "LLL" not in s
o

