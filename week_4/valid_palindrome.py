class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new_string = []
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                new_string.append(s[i])
        if len(new_string)==0:
            return True
        left = 0
        right = len(new_string)-1
        while left<right:
            if new_string[left] != new_string[right]:
                return False
            left+=1
            right-=1
        return True