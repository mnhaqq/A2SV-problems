class Solution:
    def splitString(self, s: str) -> bool:
        def is_valid_state(prev_num, idx):
            return idx == len(s)

        def get_candidates(prev_num, idx):
            arr = []
            for i in range(idx, len(s)):
                if idx == 0 and i == len(s) - 1:
                    break
                if idx == 0:
                    arr.append((int(s[:i+1]), i+1))
                elif int(s[idx:i+1]) == prev_num-1:
                    arr.append((int(s[idx:i+1]), i+1))
            return arr

        def search(prev_num, idx):
            nonlocal solutions
            if is_valid_state(prev_num, idx):
                solutions = True
                return

            for prev, i in get_candidates(prev_num, idx):
                search(prev, i)

        solutions = False
        search(-1, 0)       
        return solutions      