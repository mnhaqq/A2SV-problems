class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def is_valid_state(state):
            return len(state) == len(nums)

        def get_candidates(state):
            global_state = []
            if len(state) == 0:
                i = 0
            else:
                i = nums.index(state[-1]) + 1
            while len(state) + len(global_state) < len(nums):
                if nums[i % len(nums)] not in state:
                    global_state.append(nums[i % len(nums)])
                i += 1
            return global_state

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())

            for candidate in get_candidates(state):
                state.append(candidate)
                search(state, solutions)
                state.pop()

        solutions = []
        state = []
        search(state, solutions)
        return solutions