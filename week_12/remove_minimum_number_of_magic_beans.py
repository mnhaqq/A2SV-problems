class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        possible_answers = []
        for i in range(len(beans)):
            possible_answers.append(total-(beans[i]*(len(beans)-i)))
        return min(possible_answers)