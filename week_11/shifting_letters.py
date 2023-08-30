class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabets = list(string.ascii_lowercase)

        new_string = ""
        shifts.reverse()
        print(shifts)
        pr_sum = [0] * (len(s))
        pr_sum[0] = shifts[0]
        for i in range(1, len(pr_sum)):
            pr_sum[i] = pr_sum[i-1] + shifts[i]
        pr_sum.reverse()
        print(pr_sum)
        for i in range(len(s)):
            idx = alphabets.index(s[i])
            new_string += alphabets[(idx+pr_sum[i])%26]
        return new_string