class Solution {
    public int mySqrt(int x) {
        if (x < 2) return x;

        int left = 1, right = x / 2, result = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Use long to avoid overflow when squaring
            long square = (long) mid * mid;

            if (square == x) {
                return mid;
            } else if (square < x) {
                result = mid; // possible answer
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }
}
