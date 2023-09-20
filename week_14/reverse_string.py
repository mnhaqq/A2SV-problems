class Solution:
    def reverseString(self, s: List[str]) -> None:
        def reverse(self, left, right):
            if left >= right:
                return
            reverse(self, left+1, right-1)
            s[left], s[right] = s[right], s[left]
        reverse(self, 0, len(s)-1)
