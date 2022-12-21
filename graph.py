from collections import deque
from collections import defaultdict

class Graph:
    def __init__(self, nodes: int) -> None:
        self.N = nodes
        self.graph = defaultdict(list)
        self.weights = dict()

    def __repr__(self) -> str:
        return self.graph.__repr__()

    def addEdge(self,node,adjacent_node,weight=1) -> None:
        self.graph[node].append(adjacent_node)  
        self.weights[(node, adjacent_node)] = weight
        self.weights[(adjacent_node, node)] = weight

    def bfs(self, source: int) -> None:
        """Implementation of BFS using a queue data structure"""
        visited = [False for _ in range(self.N)]
        queue = deque()
        queue.append(source)
        visited[source] = True
        while queue:
            node = queue.popleft()
            print(node)
            for i in self.graph[node]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    
    def dfs(self, source: int) -> None:
        """Implementation of DFS using a stack data structure"""
        visited = [False for _ in range(self.N)]  
        stack = deque()
        self.dfs_util(source, visited, stack)

    def dfs_util(self, source: int, visited: list, stack: list) -> None:
        stack.append(source)
        visited[source] = True
        print(source)
        for i in self.graph[source]:
            if visited[i] == False:
                self.dfs_util(i, visited, stack)
        stack.pop()    

    def printAllPaths(self, source: int, dest: int) -> None:
        """Find all paths from source to destination using DFS"""
        visited = [False for _ in range(self.N)]
        path = deque()
        self.printAllPathsUtil(source, dest, visited, path)                      
       
    def printAllPathsUtil(self, source: int, dest: int, visited: list, path: list) -> None:   
        visited[source] = True
        path.append(source)
        if source == dest:
            print(path)
        else:
            for i in self.graph[source]:
                if visited[i] == False:
                    self.printAllPathsUtil(i, dest, visited, path) 
        path.pop()
        visited[source] = False

    def shortest_path(self, src: int, dest: int) -> None:
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        source = src
        shortest_paths = {source: (None, 0)}
        visited = [False for _ in range(self.N)]
        while source != dest:
            visited[source] = True
            weight_to_current_node = shortest_paths[source][1]
            for i in self.graph[source]:
                weight = self.weights[source, i] + weight_to_current_node
                if i not in shortest_paths:
                    shortest_paths[i] = (source, weight)
                else:
                    current_shortest_weight = shortest_paths[i][1]
                    if current_shortest_weight > weight:
                        shortest_paths[i] = (source, weight)
            
            next_destinations = { node: shortest_paths[node] for node in shortest_paths if visited[node] == False}
            if not next_destinations:
                return "Route Not Possible"
            # next node is the destination with the lowest weight
            source = min(next_destinations, key=lambda k: next_destinations[k][1])
       
        path = []
        while source is not None:
            path.append(source)
            next_node = shortest_paths[source][0]
            source = next_node
        # Reverse path
        path = path[::-1]
        
        print(f'Shortest path from {src} to {dest}: {path}')
   
if __name__ == '__main__':
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 0)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 1)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    g.addEdge(3, 1)
    g.addEdge(3, 7)
    g.addEdge(4, 1)
    g.addEdge(4, 7)
    g.addEdge(5, 2)
    g.addEdge(5, 7)
    g.addEdge(6, 2)
    g.addEdge(7, 3)
    g.addEdge(7, 4)
    g.addEdge(7, 5)

    print(g)
    # g.bfs(2)
    # g.printAllPaths(0,7)
    # g.dfs(2)
    g.shortest_path(2,7)