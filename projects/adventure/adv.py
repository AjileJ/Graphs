from room import Room
from player import Player
from world import World

from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk

traversal_path = []  #n , n
stack = Stack()

visited = set()  #v = 0, 1 , 2
stack.push(0)

while len(visited) < len(room_graph): # true keep going  set() < 9 
    current_room = stack.stack[-1]  # current_room = 0, 1, 2
    print('current room',stack.stack[-1])
    visited.add(current_room)  # visited = set(0,1)
    print('visited1', visited)
    neighbors = room_graph[current_room][1] # neighbors = {n:1}// {s:0, n:2}// {s:1}
    print('neighbors',room_graph[current_room][1])
    not_visited = []  # [1,n ] [0:s, 2: n]  []
    for direction, room_id in neighbors.items():  
        print('neighbors dict',neighbors.items())
        print('neighbors room id', room_id)
        print('direction', direction)
        if room_id not in visited:  # if 1 not in visited: checks if neighbors id is in vis.
            not_visited.append((room_id,direction)) # not_visited = [(1,n)]: append id/direc
            print('not visited', not_visited)
    if len(not_visited) > 0:  
        stack.push(not_visited[0][0])   # stack pushes 1 onto stack stack=[1]//stack[1,2]
        print('not visited[0][0]', not_visited[0][0])
        traversal_path.append(not_visited[0][1])   # appends n to traversal path
        print('not visited[0][1]', not_visited[0][1])
        print('visited2', visited)          
        # now we put last number in stack as current_room
    else:
        print('stack before pop',stack.stack)
        stack.pop()
        for direction, room_id in neighbors.items():
            if room_id == stack.stack[-1]: # if neighbors id is == last item in stack, append the direction
                print('dirdir', direction)
                print('stack ' ,stack.stack)
                print('last in stack', stack.stack[-1])
                traversal_path.append(direction)
                print('traversal path', traversal_path)   
                print('visited3', visited)        
        
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
