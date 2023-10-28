class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def is_valid_state(state):
            return len(state) == k

        def get_candidates(state):
            if len(state) == 0:
                global_state = set([i for i in range(1, n+1)])
            else:
                global_state = set([i for i in range(max(list(state)), n+1)])
                
            return global_state.difference(state)

        def search(state, solutions):
            if is_valid_state(state):
                solutions.append(state.copy())

            for candidate in get_candidates(state):
                state.add(candidate)
                search(state, solutions)
                state.remove(candidate)

        solutions = []
        state = set()
        search(state, solutions)
        return solutions