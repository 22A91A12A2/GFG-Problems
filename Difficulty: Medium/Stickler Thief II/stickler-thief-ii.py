class Solution:
    def maxValue(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return 0
        if n == 1:
            return arr[0]
        
        def solve_space(s, e):
            a = 0
            b = 0
            for i in range(e-1, s-1, -1):
                inc = arr[i]
                if i + 2 < e:
                    inc += b
                exc = a
                curr = max(inc, exc)
                b, a = a, curr
            return a
        
        l = solve_space(0, n-1)
        r = solve_space(1, n)
        return max(l, r)
#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends