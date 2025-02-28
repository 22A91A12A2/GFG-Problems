#User function Template for python3

class Solution:
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self, n):
        # code here
        x=0
        while 2**x<=n:
            if 2**x==n:
                return True
            x+=1
        return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        n = int(input())
        ob = Solution()
        if ob.isPowerofTwo(n):
            print("true")
        else:
            print("false")

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends