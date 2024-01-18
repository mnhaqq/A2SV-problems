from heapq import heapify, heappush, heappop

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        for i in range(len(tasks)):
            tasks[i].append(i)
            
        heapify(tasks)
        available_tasks = []
        curr_time = tasks[0][0]
        ans = []

        while tasks or available_tasks:
            while tasks and tasks[0][0] <= curr_time:
                enq, pro, i = heappop(tasks)
                heappush(available_tasks, (pro, i))

            if available_tasks:
                pro, i = heappop(available_tasks)
                ans.append(i)
                curr_time += pro
            elif tasks:
                curr_time = tasks[0][0]
        return ans