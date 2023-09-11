from maze import Maze
import sys

print("Welcome to 2D maze! The maze default size is 20x20, for different sizes add an integer command line argument!")

mazeSize = 20

if (len(sys.argv) > 1):
    print(sys.argv)
    if (isinstance(sys.argv[1], str)): # Not properly error checked entirely! 
        mazeSize = int(sys.argv[1])
        
maze = Maze(mazeSize)
maze.generate_maze()
maze.print()

#duh
