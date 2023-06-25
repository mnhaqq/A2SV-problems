class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i = 0
            j = len(row)-1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i+=1
                j-=1
        for row in image:
            for i in range(len(row)):
                if row[i] == 0:
                    row[i] = 1
                else:
                    row[i] = 0
        return image