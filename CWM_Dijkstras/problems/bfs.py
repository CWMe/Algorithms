from collections import deque

# Traditional BFS using a queue.
def bfs(grid, start, end, viz=None):
    Q = deque([(0, start, [])])
    visited = set()
    while Q:
        distance, location, path = Q.popleft()

        # Don't loop back
        if location in visited:
            continue
        visited.add(location)

        # End as soon as we get to destination
        if location == end:
            return distance, path

        for neighbor_info in grid.get_neighbors(location):
            neighbor_location, neighbor_cost = neighbor_info
            if neighbor_location not in visited:
                # There are better ways to do the path without lots of copies.
                # This is done for the visualization to show inbetween steps.
                new_path = path.copy()
                new_path.append(neighbor_location)
                Q.append((distance + neighbor_cost, neighbor_location, new_path))
    
