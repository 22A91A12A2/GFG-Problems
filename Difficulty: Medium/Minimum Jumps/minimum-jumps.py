class Solution:
	def minJumps(self, arr):
	    # code here
        count=x=y=0
        for i in range(len(arr)-1):
            y=max(y,arr[i]+i)
            if(x==i):
                if(y==i):
                    return -1
                count+=1
                x=y
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends