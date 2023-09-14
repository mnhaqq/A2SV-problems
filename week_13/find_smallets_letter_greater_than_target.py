class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        alphabets = list(string.ascii_lowercase)
        alphabets = alphabets[alphabets.index(target)+1:]
        i = 0
        while i < len(alphabets):
            n_target = alphabets[i]
            low, high = 0, len(letters)-1
            while low <= high:
                mid = (low + high) // 2
                if letters[mid] > n_target:
                    high = mid - 1
                elif letters[mid] < n_target:
                    low =  mid + 1
                else:
                    return n_target
            i+=1
        return letters[0]