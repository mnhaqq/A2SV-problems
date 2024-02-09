class Solution:
    def divideArray(self, nums: list[int], k: int) -> list[list[int]]:
        nums.sort()
        ans = []

        i = 0
        while i < len(nums):
            arr = []
            while i < 3 * (len(ans) + 1):
                if (arr and (nums[i] - arr[0]) > k):
                    return []
                else:
                    arr.append(nums[i])
                i += 1
            ans.append(arr)
        return ans