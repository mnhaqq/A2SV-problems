class Solution:
    def compare(self, num1, num2):
        num1 = str(num1)
        num2 = str(num2)
        if int(num1+num2) < int(num2+num1):
            return True
        return False

    def largestNumber(self, nums: List[int]) -> str:
        size = len(nums)
        tmp = list(set(nums))
        if len(tmp) == 1 and tmp[0]==0:
            return "0"
        for i in range(size):
            for j in range(size-i-1):
                if self.compare(nums[j], nums[j+1]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]

        return ''.join(map(str, nums))