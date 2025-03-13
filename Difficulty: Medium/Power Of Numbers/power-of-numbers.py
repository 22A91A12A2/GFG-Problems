#User function Template for python3

class Solution:
    def reverse_exponentiation(self, n):
        # code here
        v=int(str(n)[::-1].lstrip('0'))
        return pow(n,v)


#{ 
 # Driver Code Starts
# Input handling
if __name__ == "__main__":
    T = int(input())  # test cases

    for _ in range(T):
        n = int(input())  # input N
        solution = Solution()
        ans = solution.reverse_exponentiation(n)
        print(ans)

# } Driver Code Ends