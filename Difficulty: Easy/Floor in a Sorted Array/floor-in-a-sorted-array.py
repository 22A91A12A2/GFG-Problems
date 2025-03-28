class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        l , h = 0 , len(arr) - 1
        f = -1 
        
        while l <= h:
            mid = (l+h) // 2
            if arr[mid] <= x:
                f = mid
                l = mid +1
            else:
                h = mid -1 
        
        return f


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        x = int(input().strip())
        ob = Solution()
        ans = ob.findFloor(arr, x)
        print(ans)
        tc -= 1

# } Driver Code Ends