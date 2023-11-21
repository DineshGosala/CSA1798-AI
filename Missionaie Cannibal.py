def is_valid(state):
    m, c, b = state
    return 0 <= m <= 3 and 0 <= c <= 3 and (m == 0 or m >= c) and (3 - m == 0 or (3 - m) >= (3 - c))
def generate_successors(state):
    successors = []
    m, c, b = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for m_delta, c_delta in moves:
        new_state = (m + m_delta * (-1) ** b, c + c_delta * (-1) ** b, 1 - b)
        if is_valid(new_state):
            successors.append(new_state)
    return successors
def depth_first_search(state, path, visited):
    if state == (0, 0, 0):
        return path + [state]
    visited.add(state)
    for successor in generate_successors(state):
        if successor not in visited:
            solution = depth_first_search(successor, path + [state], visited)
            if solution:
                return solution
    return None
def print_solution(path):
    for state in path:
        print(f"Left Bank: {state[0]} missionaries, {state[1]} cannibals | Boat: {'Left' if state[2] == 0 else 'Right'}")
def main():
    initial_state = (3, 3, 1)  # Initial state: 3 missionaries, 3 cannibals, boat on the right
    visited = set()
    solution = depth_first_search(initial_state, [], visited)
    if solution:
        print("Solution found:")
        print_solution(solution)
    else:
        print("No solution found")
if __name__ == "__main__":
      main()
