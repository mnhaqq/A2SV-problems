class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low, high = 0, len(citations)-1
        h_index = 0
        while low <= high:
            mid = (low+high) //  2
            if (len(citations)-mid) <= citations[mid]:
                h_index = len(citations) - mid
                high = mid - 1
            else:
                low = mid + 1
        return h_index