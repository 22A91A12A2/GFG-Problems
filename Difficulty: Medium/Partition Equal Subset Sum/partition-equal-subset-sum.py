class Solution:
    def equalPartition(self, arr):
        # code here
        s = sum(arr)
        if s % 2:
            return False  
        target, res = s // 2, {0}
        for i in arr:
            res |= {i + x for x in res}
            if target in res:
                return True
        return False


#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends