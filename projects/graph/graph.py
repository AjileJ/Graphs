"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


#self.vertices = {"A": set(), "B": set()}
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
                        
    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
           self.vertices[v1].add(v2)
        else:
            print("error: vertex does not exist")       

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print('Error getting neighbors')

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        queue = Queue()
        # make a set for the visited nodes
        visited = set()
        # put our starting node in line
        queue.enqueue(starting_vertex)
        # while queue is not empty we need to visit more people!
        while queue.size() > 0:
            # get the next node out of line
            current_node = queue.dequeue()
            
            # check if it has been visited
            if current_node not in visited:
                ## if not, mark as visited and print current node
                visited.add(current_node)
                print(current_node)
                ## and get its neighbors
                edges = self.get_neighbors(current_node)
                ## loop through edges(connections)
                for edge in edges:
                    ## put them in line to be visited
                    queue.enqueue(edge)
                    
                    
    # def dft(self, starting):
    #     s = Stack()
    #     vis = set()
    #     s.push(starting)
    #     while s.size() > 0:
    #         current = s.pop()
    #         if current not in vis:
    #             vis.add(current)
    #             print(current)
    #             ed = self.get_neighbors(current)
    #             for e in ed:
    #                 s.push(e)
                
            
            
                             
            
            
            

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        stack = Stack()
        # make a set for the visited nodes
        visited = set()
        # put our starting node on top of stack
        stack.push(starting_vertex)
        # while stack is not empty we need to visit more people!
        while stack.size() > 0:
            # get the next node out of the top of stack
            current_node = stack.pop()
            
            # check if it has been visited
            if current_node not in visited:
                ## if not, mark as visited and print current node
                visited.add(current_node)
                print(current_node)
                ## and get its neighbors
                edges = self.get_neighbors(current_node)
                ## loop through edges(connections)
                for edge in edges:
                    ## stack them on stack to be visited
                    stack.push(edge)
        

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        
        """
        if visited is None:
            visited = set()
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            edges = self.get_neighbors(starting_vertex)
        
        if len(edges) == 0:
            return
        else:
            for edge in edges:
                if edge not in visited:
                    self.dft_recursive(edge, visited)
                else:
                    return 
              
         
                    
                    
        #dft_recursive(1, set())
        #visited = set(1,2,3,5,4,7,6)
        #edges = set(2)            
        #dft_recursive(2, set(1,2,3,5))
        #visited = set(1,2,3,5,4,7)
        #edges = set(4)
        #dft_recursive(4,set(1,2,3,5))
        #visited = set(1,2,3,5,4,7)
        #edges=(set(6,7))
        #dft_recursive(7, set(1,2,3,4,5))
        #visited = set(1,2,3,5,4,7)
        #edges = set(6,1)
        #dft_recursive(6, set(1,2,3,5,4,7))
        #visited = set(1,2,3,5,4,7,6)
        #edges = set(3)
        #dft_recursive(1, set(1,2,3,5,4,7,6))
        #visited = set(1,2,3,5,4,7,6)
        #edges = set(2)
        
                    
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breadth-first order.
        """
        # make a queue
        queue = Queue()
        # make a set for visited = visited = set()
        visited = set()
        
        #enqueue a PATH TO the starting_vertex
        queue.enqueue([starting_vertex])
        
        # while the queue is not empty:
        while queue.size() > 0:
            ## dequeue the next path
            current_path = queue.dequeue()
            ## current_node is the last thing in the path
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            else:
                if current_node not in visited:
                    visited.add(current_node)
                    edges = self.get_neighbors(current_node)
                    
                    for edge in edges:
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        queue.enqueue(path_copy)
                
            ## check if its the target , aka the destiniation_vertex
            ## if so, return the path!!
            ## if not, mark this as visited 
            ## get the neighbor to the copy
            ## for each one, add a PATH TO IT to our queue 
        
             
           

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # make a stack
        stack = Stack()
        # make a set for visited = visited = set()
        visited = set()
        
        #enqueue a PATH TO the starting_vertex
        stack.push([starting_vertex])
        
        # while the queue is not empty:
        while stack.size() > 0:
            current_path = stack.pop()
            ## current_node is the last thing in the path
            current_node = current_path[-1]
            if current_node == destination_vertex:
                return current_path
            else:
                if current_node not in visited:
                    visited.add(current_node)
                    edges = self.get_neighbors(current_node)
                    
                    for edge in edges:
                        path_copy = list(current_path)
                        path_copy.append(edge)
                        stack.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):               #dfs_recursive(1,6)         (2, 6, {1}, [1])        (3, 6, {1,2})
            """
            Return a list containing a path from
            starting_vertex to destination_vertex in
            depth-first order.
            This should be done using recursion.
            """
            
            if visited is None:
                visited = set()
            if path is None:
                path = []    
            visited.add(starting_vertex)                                                          # {1}                      {1,2}                    {1,2,3}
            path = path + [starting_vertex]                                                       # path = [1]               [1, 2]                   [1,2,3]
            if starting_vertex == destination_vertex:                                             # 1 == 6 / False           2 == 6 / False           3 == 6 / False
                return path                                                                       # [1,2,4,6]                
            for vert in self.vertices[starting_vertex]:                                           # self.vertices[1] = {2}   {3, 4}                   {5}
                if vert not in visited:                                                           # 2 not in [1] / True       3 not in [1, 2] /True   5 not in [1,2, 3]
                    final_path = self.dfs_recursive(vert, destination_vertex, visited, path)
                    if final_path:                                                                          # [1,2,4,6]
                        return final_path
            else:
                return None        
            

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)
    

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
