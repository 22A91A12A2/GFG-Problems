class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        import heapq
        pairs = sorted(zip(deadline, profit), key=lambda x: (x[0], -x[1]))
        h, res = [], 0
        for a,b  in pairs:
            if a > res:
                res += 1
                heapq.heappush(h, b)
            elif a == res:
                heapq.heappushpop(h, b)
        return len(h), sum(h)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends