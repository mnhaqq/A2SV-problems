class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        left, right = 1, len(skill) -2
        chemistry = skill[0] * skill[len(skill)-1]
        target = skill[0] + skill[len(skill)-1]
        while left < right:
            if target != skill[left] + skill[right]:
                return -1
            else:
                chemistry += skill[left] * skill[right]
            left+=1
            right-=1
        return chemistry
