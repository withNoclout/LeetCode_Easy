class Solution {
    public int climbStairs(int n) {
        if (n <= 2) {
            System.out.println("Base case: n = " + n + " → ways = " + n);
            return n;
        }

        int oneStepBefore = 2;
        int twoStepsBefore = 1;
        int result = 0;

        System.out.println("Starting iteration from 3 to " + n);
        for (int i = 3; i <= n; i++) {
            result = oneStepBefore + twoStepsBefore;
            System.out.println("Step " + i + ": " + oneStepBefore + " (1-step before) + "
                               + twoStepsBefore + " (2-steps before) = " + result);
            twoStepsBefore = oneStepBefore;
            oneStepBefore = result;
        }

        System.out.println("Total ways to climb " + n + " stairs: " + result);
        return result;
    }
}
