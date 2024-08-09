class Solution:
    def isValid(self, s: str) -> bool:
        valid = ["()", "[]", "{}"]
        tries = 10000

        for j in range(tries):
            for i in valid:
                if i in s:
                    s = s.replace(i, "")

        if s != "":
            return False

        return True


sol = Solution()

s = "([])"

print(sol.isValid(s))

# 1 <= s.length <= 10^4