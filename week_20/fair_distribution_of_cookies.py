class Solution:
    def distributeCookies(self, cookies: list[int], k: int) -> int:
        #initialize state array to hold number of cookies each child has
        state = [0]*k

        #at the beginning ans is assigned the sum of cookies which is the worst possible answer
        ans = sum(cookies)
        
        def search(state, idx):
            #ans is made nonlocal so its available on a recursive call stacks
            nonlocal ans

            #this codition checks whether each child has been given a cookie
            #this must happen for us to have a valid answer
            #if this condition is true, we reassign our answer
            if idx == len(cookies):
                ans = min(ans, max(state))
                return
            
            #this for loop iterates through the state array
            #and the state array represents the number of cookies each child has
            for i in range(k):
                #we give cookies[idx] to our current child
                state[i] += cookies[idx]

                #if the number of cookies our current child has is greater than our current
                # minimum unfairness there's no need to continue that route
                if state[i] < ans:
                    #we use this recursive call to iterate through our array of cookies
                    search(state, idx+1)
                #taking back the cookie we gave to our current child
                state[i] -= cookies[idx]
        
        #search function is called with idx at 0
        #idx represents the i'th cookie so it starts at 0 which represents 0th cookie
        search(state, 0)
        return ans