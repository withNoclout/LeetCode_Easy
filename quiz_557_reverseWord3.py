class Solution:
    def reverseWords(self, s):
        words = s.split()  # แยก string เป็นคำ ๆ
        reversed_words = [word[::-1] for word in words]  # กลับตัวอักษรของแต่ละคำ
        return ' '.join(reversed_words)  # รวมกลับเป็นประโยคo

