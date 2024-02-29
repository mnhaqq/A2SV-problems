class Solution:
    def __init__(self):
        self.root = {}
    

    def add_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]

    def findMaximumXOR(self, nums: List[int]) -> int:
        bit_len = max(nums).bit_length()
        nums = [bin(num)[2:] for num in nums]
        nums = [("0" * (bit_len - len(num))) + num for num in nums]

        for num in nums:
            self.add_word(num)
        
        res = 0
        for num in nums:
            check = ""
            i = 0
            curr = self.root
            while curr:
                if len(curr) > 1:
                    if num[i] == '0' and '1' in curr:
                        check += '1'
                        curr = curr['1']
                    elif num[i] == '1' and '0' in curr:
                        check += '0'
                        curr = curr['0']
                elif len(curr) == 1:
                    key = list(curr.keys())[0]
                    check += key
                    curr = curr[key]
                i += 1
            res = max(res, int(num, 2) ^ int(check, 2))
            
        return res

