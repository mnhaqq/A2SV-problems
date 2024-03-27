class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 2)

        for a, b, c in shifts:
            if c == 1:
                arr[a+1] += 1
                arr[b+2] -= 1
            else:
                arr[a+1] -= 1
                arr[b+2] += 1
        
        for i in range(1, len(arr)):
            arr[i] += arr[i-1]
        
        ans = ""
        for i in range(len(s)):
            val = ord(s[i]) - ord('a')
            val += arr[i+1]
            val %= 26
        
            ans += chr(val + ord('a'))
            
        return ans
