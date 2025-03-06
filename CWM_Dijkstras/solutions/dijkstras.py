from collections import defaultdict
from heapq import heappop, heappush, heapify

# https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def djikstra(grid, start, end, viz=None):
    Q = [(0, start, [])]
    heapify(Q)
    dist = defaultdict(lambda: 1e6)
    dist[start] = 0
    while len(Q):
        distance, location, path = heappop(Q)
        if viz:
            viz.add_frame(distance, location, path, Q, dist)
      
        if distance > dist[location]:
            continue
        
        if location == end:
            return distance, path, dist

        for neighbor_info in grid.get_neighbors(location):
            neighbor_location, neighbor_cost = neighbor_info
            neighbor_distance = distance + neighbor_cost
            if neighbor_distance < dist[neighbor_location]:
                dist[neighbor_location] = neighbor_distance
                new_path = path.copy()
                new_path.append(neighbor_location)
                heappush(Q, (neighbor_distance, neighbor_location, new_path))