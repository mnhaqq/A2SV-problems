class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def is_valid_state(state):
            return len(state) == len(nums)

        def get_candidates(state):
            global_state = []
            for i in range(len(nums)):
                if nums[i] not in state:
                    global_state.append(nums[i])
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