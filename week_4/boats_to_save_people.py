class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        count = people.count(limit)
        people = [i for i in people if i != limit]
        people.sort()
        left=0
        right=len(people)-1
        pairs=0
        print(people)
        while left < right:
            if people[left]+people[right]==limit:
                pairs+=2
                count+=1
                left+=1
                right-=1
            elif people[left]+people[right]<limit:
                right-=1
                left+=1
                pairs+=2
                count+=1
            else:
                right-=1
        count+=len(people)-pairs
        return count
        