from collections import deque

def water_jug_problem(capacity_jug1, capacity_jug2, target_amount):
    visited_states = set()
    initial_state = (0, 0)

    queue = deque([initial_state])
    visited_states.add(initial_state)

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        if jug1 == target_amount or jug2 == target_amount:
            print("Solution found:")
            print_path(current_state, initial_state)
            return

        fill_jug1 = (capacity_jug1, jug2)
        enqueue_state(fill_jug1, queue, visited_states, current_state)

        fill_jug2 = (jug1, capacity_jug2)
        enqueue_state(fill_jug2, queue, visited_states, current_state)

        empty_jug1 = (0, jug2)
        enqueue_state(empty_jug1, queue, visited_states, current_state)

        empty_jug2 = (jug1, 0)
        enqueue_state(empty_jug2, queue, visited_states, current_state)

        pour_jug1_to_jug2 = (
            max(0, jug1 - (capacity_jug2 - jug2)),
            min(capacity_jug2, jug1 + jug2),
        )
        enqueue_state(pour_jug1_to_jug2, queue, visited_states, current_state)

        pour_jug2_to_jug1 = (
            min(capacity_jug1, jug1 + jug2),
            max(0, jug2 - (capacity_jug1 - jug1)),
        )
        enqueue_state(pour_jug2_to_jug1, queue, visited_states, current_state)

def enqueue_state(state, queue, visited_states, parent_state):
    if state not in visited_states:
        queue.append(state)
        visited_states.add(state)
        parent_map[state] = parent_state

def print_path(current_state, initial_state):
    path = []
    while current_state != initial_state:
        path.append(current_state)
        current_state = parent_map[current_state]
    path.append(initial_state)
    path.reverse()

    for state in path:
        print(state)

if __name__ == "__main__":
    jug1_capacity = 4
    jug2_capacity = 3
    target_amount = 2

    parent_map = {}

    water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
