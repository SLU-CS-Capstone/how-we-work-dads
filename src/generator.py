from maze import Maze
from pypdf import PdfReader
page = pdf_writer.add_blank_page(width=8.27 * 72, height=11.7 * 72)
#making changes to my code
maze = Maze(20)
maze.generate_maze()
maze.print()
print("Welcome to 2D maze")
