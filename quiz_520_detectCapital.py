class Solution:
    def detectCapitalUse(self, word):
        # ใช้ฟังก์ชันในตัวของ Python ตรวจสอบแต่ละกรณี
        return word.isupper() or word.islower() or word.istitle()
