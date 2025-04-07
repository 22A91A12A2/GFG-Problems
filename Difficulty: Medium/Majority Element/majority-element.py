#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        from collections import Counter
        #code here
        count = Counter(arr)
        n = len(arr)
        for key,val in count.items():
            if val > n/2:
                return key
        return -1     


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends