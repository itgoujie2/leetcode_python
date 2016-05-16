public class Solution {
    public int numSquares(int n) {
        Double temp = new Double(Math.floor(Math.sqrt(n)));
        int size = temp.intValue();
        int[] dp = new int[n+1];
        for (int i = 0; i < dp.length; i++){
            dp[i] = Integer.MAX_VALUE;
        }
        dp[0] = 0;
        for (int i = 1; i <= n; i++){
            for (int j = 1; j <= size; j++ ){
                if ( i - j*j >= 0){
                    dp[i] = Math.min(dp[i], dp[i - j*j] + 1);    
                }
            }
        }
        
        return dp[n];
    }
}