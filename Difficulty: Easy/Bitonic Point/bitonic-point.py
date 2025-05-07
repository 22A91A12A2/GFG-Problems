#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		for i in range(len(arr)):
		    if arr[i+1]<arr[i]:
		        return arr[i]
		    else:
		        x=arr[i]
		return x


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends