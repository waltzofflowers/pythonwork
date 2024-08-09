class Solution():
    def isPalindrome(self, num):
        num = str(num)
        if num == num[::-1]:
            return True
        else:
            return False

sol = Solution()

num = 1221

print(sol.isPalindrome(num))