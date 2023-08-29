class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dic = dict()
        for pair in knowledge:
            dic[pair[0]] = pair[1]
        new_s=""
        i = count = 0
        while i < len(s):
            if s[i] == "(":
                i+=1
                curr = ""
                while s[i] != ")":
                    curr +=s[i]
                    i+=1
                if curr in dic:
                    new_s+=dic.get(curr)
                else:
                    new_s+="?"
            else:
                new_s += s[i]
            i+=1
        return new_s