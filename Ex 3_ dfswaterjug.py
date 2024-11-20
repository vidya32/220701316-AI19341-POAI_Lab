from collections import deque

def DFS(a, b, target):
    m = {}
    is_solvable = False
    path = []
    q = deque()
    q.append((0, 0))

    while q:
        u = q.popleft()
        if (u[0], u[1]) in m:
            continue
        if u[0] > a or u[1] > b or u[0] < 0 or u[1] < 0:
            continue
        path.append([u[0], u[1]])
        m[(u[0], u[1])] = 1

        if u[0] == target or u[1] == target:
            is_solvable = True
            if u[0] == target and u[1] != 0:
                path.append([u[0], 0])
            elif u[0] != 0 and u[1] == target:
                path.append([0, u[1]])

            for i in range(len(path)):
                print("(", path[i][0], ",", path[i][1], ")")
            break

        q.append([u[0], b])
        q.append([a, u[1]])

        for ap in range(max(a, b) + 1):
            c = u[0] + ap
            d = u[1] - ap
            if c <= a and d >= 0:
                q.append([c, d])

            c = u[0] - ap
            d = u[1] + ap
            if c >= 0 and d <= b:
                q.append([c, d])

        q.append([a, 0])
        q.append([0, b])

    if not is_solvable:
        print("No solution")

Jug1, Jug2, target = 4, 3, 2
print("Path from initial state to solution state ::")
DFS(Jug1, Jug2, target)
