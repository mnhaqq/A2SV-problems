from collections import deque

class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)

        arr = deque(arr)
        curr_wins = 0
        winner = arr[0]
        while curr_wins < k:
            if arr[0] > arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
                num = arr.popleft()
                arr.append(num)
                curr_wins += 1
            else:
                num = arr.popleft()
                arr.append(num)
                curr_wins = 1
                winner = arr[0]
        return winner