class Solution:
    def maxProfit(self, prices):
        # code here
        if not prices:
            return 0
        a = float('inf')
        cnt = 0
        b = float('inf')
        res = 0
            
            
        for i in prices:
            a = min(a, i)
            cnt = max(cnt , i - a)
            
            b = min(b, i - cnt)
            res = max(res, i - b)
                
                
        return res


#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends