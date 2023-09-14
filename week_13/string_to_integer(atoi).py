class Solution:
    def myAtoi(self, s: str) -> int:
        new_s = ""
        status = False
        for i in range(len(s)):
            if s[i] == " ":
                continue
            elif s[i] == "-":
                if i+1 < len(s) and not s[i+1].isdigit():
                    break
                new_s += s[i]
            elif s[i] == "+":
                if i+1 < len(s) and not s[i+1].isdigit():
                    break
            elif not s[i].isdigit():
                break
            while i < len(s) and s[i].isdigit():
                status = True
                new_s += s[i]
                i+=1
            if status:
                break
        if not new_s or new_s == "-":
            return 0
        num = int(new_s)
        if num < -2**31:
            num = -2**31
        elif num > 2**31 - 1:
            num = 2**31 -1
        return num
        