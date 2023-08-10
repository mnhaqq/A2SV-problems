class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        a palindrome is a string which is a mirror image
        that means anything that appears on the left side appears on the right

        so my approach was to use the number of times each character appears in s
        if a character appears an even number of times, that means all those
        characters can form a palindrome since we can match each character on left
        and right

        but if a character appears an odd number of times we can use an even number
        of characters to form a palindrome (the number of characters minus one)

        at the end if we have several characters appearing an odd number of times
        we can use just one of the extra characters as the center of the palindrome
        """
        longest = 0
        #create a counter to count the number of times
        #each character appears
        dic = Counter(s)

        #create variable status which checks if there's any
        #character which occurs odd number of times
        status = False
        for key, value in dic.items():
            #if the number of times a character appears is even
            #that means we can use each one to form a palindrome
            if value % 2 == 0:
                longest+=value
            #if the number of times a character appears is odd that means
            #we have one extra character we cannot use
            else:
                status = True
                longest+=value-1
        #if we have several characters appearing an odd number of times
        #we can use just one of them as the center character
        if status:
            longest+=1
        return longest