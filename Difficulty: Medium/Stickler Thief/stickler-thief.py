class Solution:  
    def findMaxSum(self,arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
        if n ==1:
            return arr[0]
        a = arr[0]
        b= max(arr[0], arr[1])
        
        for i in range(2, n):
            cur = max(b, arr[i]+ a)
            a = b
            b= cur
            
        return b


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends