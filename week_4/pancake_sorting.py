class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def reverse_sub_array(start, end):
            while start<=end:
                print(start, end)
                arr[start], arr[end] = arr[end], arr[start]
                start+=1
                end-=1
        final=[]
        tmp = sorted(arr, reverse=True)
        i=0
        while i < len(arr):
            for j in range(len(arr)-i):
                if arr[j]==tmp[i]:
                    reverse_sub_array(0,j)
                    reverse_sub_array(0,len(arr)-i-1)
                    final.append(j+1)
                    final.append(len(arr)-i)
                    break
            i+=1
        return final
        