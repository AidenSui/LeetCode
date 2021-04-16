    def longestPalindrome(s: str) -> str:
        def longer(s1, s2):
            if len(s1) > len(s2):
                return s1
            return s2
        
        def showDp(dp):
            for i in range(len(dp)):
                print(dp[i])
            print()
    
        n = len(s)
        dp = [[0 for j in range(n)] for i in range(n+1)]
        
        showDp(dp)
        start_idx = 0
        max_len = 1
            
        for i in range(1,n+1):
            for j in range(len(s) - i + 1):
                if i == 1:
                    dp[i][j] = 1
                    dp[i-1][j] = 1
                    showDp(dp)
                    
                else:
                    print(s[j], s[i+j-1])
                    if s[j] == s[i+j-1] and dp[i-2][j+1] == 1: 
                        dp[i][j] = 1
                        start_idx = j
                        max_len = i
                        print("start index:", j, "; length:", i-1, "1")
                        showDp(dp)
    
                    
        showDp(dp)
        return s[start_idx: start_idx + max_len]

print(longestPalindrome("cbbdb"))





