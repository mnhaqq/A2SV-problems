class Solution:
    def simplifyPath(self, path: str) -> str:
        queue = deque()
        i  = 0
        while i < len(path):
            string = ""
            while i < len(path) and path[i] != "/":
                string += path[i]
                i+=1

            if queue and string == "..":
                queue.pop()
            elif string == "." or string == "..":
                pass
            elif string:
                queue.append(string)

            while i < len(path) and path[i] == "/":
                i+=1
                
        cannonical_path = ""
        for i in range(len(queue)):
            cannonical_path += "/"
            cannonical_path += queue[i]
        if not cannonical_path:
            cannonical_path += "/"
        return cannonical_path