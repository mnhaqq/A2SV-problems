class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed=[0]+flowerbed+[0]
        for i in range(1,len(flowerbed)-1):
            check = flowerbed[i-1] + flowerbed[i] + flowerbed[i+1]
            if check == 0:
                flowerbed[i] = 1
                n-=1
        return n < 1