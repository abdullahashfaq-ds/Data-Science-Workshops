"""HEURISTIC | MISPLACED TILES"""

import copy
import heapq


def print_states(state):
    for row in state:
        print(
            " ".join(map(str, row))
        )
    print()


def get_index(state, tile=0):
    n = len(state)
    for x in range(n):
        for y in range(n):
            if state[x][y] == tile:
                return x, y
    return -1


def heuristic(state):
    cost = 0
    n = len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                cost += 1
    return cost


def childs(state):
    moves = [
        (0, -1), (0, 1), (-1, 0), (1, 0)
    ]
    successor = []

    for dx, dy in moves:
        x, y = get_index(state)
        new_x, new_y = x+dx, y+dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new = copy.deepcopy(state)
            new[x][y], new[new_x][new_y] = new[new_x][new_y], new[x][y]
            successor.append(new)

    return successor


def solve(initial_state, goal_state):
    visited = set()
    queue = [
        (heuristic(initial_state), initial_state, [])
    ]

    while queue:
        _, current_state, path = heapq.heappop(queue)

        if current_state == goal_state:
            print('Goal State is found.')
            for i, steps in enumerate(path):
                print(f"Step no. {i+1}")
                print_states(steps)
            return

        visited.add(
            tuple(map(tuple, current_state))
        )

        for succerors in childs(current_state):
            if tuple(map(tuple, succerors)) not in visited:
                h = heuristic(succerors)
                heapq.heappush(
                    queue, (h, succerors, path+[succerors])
                )

    print('Goal State is not found.')
    return


if __name__ == "__main__":
    initial_state = [
        [4, 8, 3],
        [0, 5, 1],
        [6, 2, 7]
    ]
    goal_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]

    solve(initial_state, goal_state)
