class Solution(object):
    def longestCommonPrefix(self, strs):

        choose = strs[0]

        for string in strs[1:]:
            while string.find(choose) != 0:
                choose = choose[:-1]
                if not choose:
                    return ""
        return choose

sol = Solution()

strs = ["dog","racecar","car"]

print(sol.longestCommonPrefix(strs))