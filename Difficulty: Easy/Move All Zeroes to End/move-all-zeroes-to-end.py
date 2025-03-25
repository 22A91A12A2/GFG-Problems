#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	cnt = arr.count(0)
        
        res = [x for x in arr if x != 0]
        arr[len(arr)-cnt:]  = [0]*cnt 
        arr[:len(arr)-cnt] = res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends