class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "AEIOUaeiou"
        vowels = set(vowels)
        
        vowels_in_s = ""
        for i in range(len(s)):
            if s[i] in vowels:
                vowels_in_s += s[i]
        vowels_in_s = vowels_in_s[::-1]
        
        ans = ""
        vp = 0
        for i in range(len(s)):
            if s[i] in vowels:
                ans += vowels_in_s[vp]
                vp+=1
            else:
                ans += s[i]
        return ans