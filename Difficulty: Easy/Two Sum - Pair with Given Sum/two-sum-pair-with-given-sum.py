#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
        arr.sort()
        i=0
        res=len(arr)-1
        while i<res:
            a=arr[i]+arr[res]
            if a==target:
                return True
            elif a<target:
                i+=1
            else:
                res-=1
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends