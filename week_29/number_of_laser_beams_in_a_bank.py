class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        prev_row = bank[0].count("1")

        for i in range(1, len(bank)):
            curr_row = bank[i].count("1")
            if curr_row == 0:
                continue
            ans += prev_row * curr_row
            prev_row = curr_row
        return ans
