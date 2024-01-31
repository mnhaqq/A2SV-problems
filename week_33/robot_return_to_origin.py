class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]

        for move in moves:
            if move == "U":
                pos[1] += 1
            if move == "D":
                pos[1] -= 1
            if move == "L":
                pos[0] -= 1
            if move == "R":
                pos[0] += 1
        return pos == [0, 0]