#User function Template for python3

class Solution:
    def isPalindrome(self, n):
		# Code here
		c=str(n)
		if(c==c[::-1]):
		    return True
		else:
		    return False
		


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())  # Number of test cases
    solution = Solution()

    for _ in range(T):
        n = int(input())  # Input number
        ans = solution.isPalindrome(n)
        print("true" if ans else "false")

        print("~")

# } Driver Code Ends