class Solution:
    def maxProfit(self, prices, k):
        # code here
        n=len(prices)
        res=[[0] * n for _ in range(k+1)]
        if n<=1 or k ==0:
            return 0
        for i in range(1,k+1):
            d=-prices[0]
            for j in range(1,n):
                res[i][j]=max(res[i][j-1],prices[j]+d)
                d=max(d,res[i-1][j]-prices[j])
        return res[k][n-1]


#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends