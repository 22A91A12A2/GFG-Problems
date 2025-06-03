class Solution:
    def countSubstr (self, s, k):
        # Code here
        from collections import defaultdict
        
        def at_most_k(s, k):
            count = 0
            le = 0
            f = defaultdict(int)
            
            for r in range(len(s)):
                f[s[r]] += 1
                while len(f) > k:
                    f[s[le]] -= 1
                    if f[s[le]] == 0:
                        del f[s[le]]
                    le += 1
                count += r - le + 1
            return count
        
        return at_most_k(s, k) - at_most_k(s, k - 1)