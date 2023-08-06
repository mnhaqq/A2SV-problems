class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        dic=dict()
        prefix_common_arr=[]
        count=0
        for i in range(len(A)):
            dic[A[i]]=dic.get(A[i],0)+1
            dic[B[i]]=dic.get(B[i],0)+1
            if dic[A[i]]==2:
                count+=1
            if dic[B[i]]==2:
                count+=1
            if A[i]==B[i]:
                count-=1
            prefix_common_arr.append(count)
        return prefix_common_arr