class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = set()
        stack = []
        last_occ = dict()

        for i in range(len(s)):
            last_occ[s[i]] = i
        
        for i in range(len(s)):

            if s[i] in visited:
                continue
            while stack and i <= last_occ[stack[-1]] and s[i] < stack[-1]:
                visited.remove(stack[-1]) 
                stack.pop()

            visited.add(s[i])
            stack.append(s[i])
        return "".join(stack)