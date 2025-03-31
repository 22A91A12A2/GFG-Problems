class Solution:
    def maxPartitions(self , s):
        # code here
        cnt = {ch: i for i, ch in enumerate(s)}
        res, ind = 0, 0  

        for i, ch in enumerate(s):
            ind = max(ind, cnt[ch])
            if ind == i:
                res += 1  

        return res


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends