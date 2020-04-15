class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}
                        
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
           self.vertices[v1].add(v2)
        else:
            print("error: vertex does not exist")

#ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):  # earliest_ancestor(ancestors, 9)
    #build our graph
    graph = Graph()
    #grab pairs from ancestors
    for pair in ancestors:                      
        #add a vertex to each item in pair
        parent = pair[0]                     #in the ancestors array, the parent is in the 0 index and the child is in the 1 index based off graph
        child = pair[1]
        graph.add_vertex(parent)          # add a vertex to the parent and child
        graph.add_vertex(child)
        #add an edge between child and parent
        graph.add_edge(child, parent)   # create an edge between the child and parent
        
    #BFS  
#       10          # row 4
#     /
#    1   2   4  11   #row 3 
#     \ /   / \ /
#      3   5   8  #row 2
#      \ / \   \
#       6  7   9   # row 1
    
                                            # using breadth search to get the rows
    queue = Queue()                      # create a queue
    queue.enqueue([starting_node])    #  enqueue the starting node [9] / starting_node[8]/ starting_node [9,8,4,11]
    
    longest_path_length = 1          
    earliest_ancestor = -1
    
    while queue.size() > 0:          # while the queue size is not empty
        path = queue.dequeue()       # path is the dequeued item
        current_node = path[-1]      # current path is last item that was in dequeued array= 9 = 8 = 11

        if len(path) >= longest_path_length and current_node < earliest_ancestor:  # if 1 / 2 >= 1 and 9, 8 < -1 / false go to next if, false/ 4 is greater less than -1
            longest_path_length = len(path)
            earliest_ancestor = current_node
        
        if len(path) > longest_path_length:      # if 1 / 2 > 1 / false go to next if / true
            longest_path_length = len(path)     #longest_path = 2   longest path = 4
            earliest_ancestor = current_node     # earliest_ancestor = 8   e_a = 11
 
        neighbors = graph.vertices[current_node]  # neighbors = 8   /neighbors = 4,11
        for ancestor in neighbors:              
            path_copy = list(path)       #path_copy = [9]       [8]
            path_copy.append(ancestor)   #path-copy.append(8)   = path_copy[9,8] / path_copy.append(4,11) = path_copy[9,8,4,11]
            queue.enqueue(path_copy)    #enqueues [9,8]       =  enqueues [9,8, 4,11]
            
    return earliest_ancestor   

#finished 
            
            
            
            
          
        
    