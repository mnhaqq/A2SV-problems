import string

class Solution:
    def maxProduct(self, words: list[str]) -> int:
        alphabets = string.ascii_lowercase
        dic = dict()

        for i in range(len(alphabets)):
            dic[alphabets[i]] = i
        
        bin_rep = []
        for i in range(len(words)):
            curr = ['0'] * 26
            for j in range(len(words[i])):
                curr[dic[words[i][j]]] = '1'
            bin_rep.append(''.join(curr))
        
        ans = 0
        for i in range(len(bin_rep)):
            for j in range(i+1, len(bin_rep)):
                if int(bin_rep[i], 2) & int(bin_rep[j], 2) == 0:
                    ans = max(ans, len(words[i] * len(words[j])))
        return ans