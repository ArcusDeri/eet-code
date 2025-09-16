# https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1162/
class Solution:
    # Time: O(m * n), where m = length of `strs[0]` and n = length of `strs`
    # (worst case, otherwise the loop returns early)
    # Space: O(L), where L = longest common prefix length (space we need for
    # `res`)
    def longestCommonPrefix(self, strs):
        res = ""
        # Use the first string but it can be any.
        # Compare chosen string chars one by one with strings in the array
        for i in range(len(strs[0])):
            for s in strs:
                # safety net: `i` can be longer than current string
                # e.g. ["ab", "a"]. We can return then.
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
