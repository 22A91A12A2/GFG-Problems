#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        n = len(arr)
        cnt = 0
        res = 0
        i = 0
        j = 0
        
        while i < n and j < n:
            if arr[i] <= dep[j]:
                cnt += 1
                i += 1
            else:
                cnt -= 1
                j += 1
            
            res = max(res, cnt)
        
        return res 




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends