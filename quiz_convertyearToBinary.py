class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Split date into year, month, day
        year, month, day = map(int, date.split('-'))
        # Convert each part to binary and remove '0b' prefix
        year_bin = bin(year)[2:]
        month_bin = bin(month)[2:]
        day_bin = bin(day)[2:]
        # Join with '-' in between
        return f"{year_bin}-{month_bin}-{day_bin}"
