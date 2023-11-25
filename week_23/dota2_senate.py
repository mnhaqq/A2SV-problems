from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        num_radiants = senate.count("R")
        num_dires = senate.count("D")
        banned_radiants = banned_dires = 0
        queue = deque(senate)
        
        while True:
            person = queue.popleft()
            if person == "R":
                if banned_radiants > 0:
                    num_radiants -= 1
                    banned_radiants -= 1
                else:
                    queue.append(person)
                    banned_dires += 1
            elif person == "D":
                if banned_dires > 0:
                    num_dires -= 1
                    banned_dires -= 1
                else:
                    queue.append(person)
                    banned_radiants += 1
            if num_radiants == 0:
                return "Dire"
            elif num_dires == 0:
                return "Radiant"