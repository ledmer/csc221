from gasp import *    
GRID_SIZE = 40                   
MARGIN = 80             
BACKGROUND_COLOR = color.BLACK     
WALL_COLOR = '#99E5E5'              
the_layout = [
  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%",     
  "%.....%.................%.....%",
  "%o%%%.%.%%%.%%%%%%%.%%%.%.%%%o%",
  "%.%.....%......%......%.....%.%",
  "%...%%%.%.%%%%.%.%%%%.%.%%%...%",
  "%%%.%...%.%.........%.%...%.%%%",
  "%...%.%%%.%.%%% %%%.%.%%%.%...%",
  "%.%%%.......%GG GG%.......%%%.%",
  "%...%.%%%.%.%%%%%%%.%.%%%.%...%",
  "%%%.%...%.%.........%.%...%.%%%",
  "%...%%%.%.%%%%.%.%%%%.%.%%%...%",
  "%.%.....%......%......%.....%.%",
  "%o%%%.%.%%%.%%%%%%%.%%%.%.%%%o%",
  "%.....%........P........%.....%",
  "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"]
class Immovable:
    pass                                   # We have nothing to put in this class yet

class Nothing(Immovable):
    pass
class Wall(Immovable):
    def __init__(self, maze, point):
        self.place = point                          # Store our position
        self.screen_point = maze.to_screen(point)
        self.maze = maze                            # Keep hold of Maze
        self.draw()

    def draw(self):
        (screen_x, screen_y) = self.screen_point
        dot_size = GRID_SIZE * 0.2
        # Just draw circle
        Circle(self.screen_point, dot_size, color=WALL_COLOR, filled=True)
class Maze:
    def __init__(self):
        self.have_window = False        # We haven't made window yet
        self.game_over = False          # Game isn't over yet
        self.set_layout(the_layout)     # Make all objects
        set_speed(20)
    def set_layout(self, layout):
        height = len(layout)                   # Length of list
        width = len(layout[0])                 # Length of first string
        self.make_window(width, height)
        self.make_map(width, height)           # Start new map
        self.make_tittle(width, height)
        max_y = height - 1
        for x in range(width):                 # Go through whole layout
            for y in range(height):
                char = layout[max_y - y][x]    # See discussion 1 page ago
                self.make_object((x, y), char)    

    def make_window(self, width, height):
        grid_width = (width - 1) * GRID_SIZE     # Work out size of window
        grid_height = (height - 1) * GRID_SIZE
        screen_width = 2 * MARGIN + grid_width
        screen_height = 4 * MARGIN + grid_height
        begin_graphics(screen_width, screen_height, BACKGROUND_COLOR, "")
    def to_screen(self, point):
        (x, y) = point
        x = x*GRID_SIZE + MARGIN     # Work out coordinates of point
        y = y*GRID_SIZE + MARGIN     # on screen
        return (x, y)  

    def make_map(self, width, height):
        self.width = width                 # Store size of layout
        self.height = height
        self.map = []                      # Start with empty list
        for y in range(height):
            new_row = []                   # Make new row list
            for x in range(width):
                new_row.append(Nothing())  # Add entry to list
            self.map.append(new_row)
    def make_tittle(self, width, height):
        grid_width = (width - 1) * GRID_SIZE     # Work out size of window
        grid_height = (height - 1) * GRID_SIZE
        screen_width = 2 * MARGIN + grid_width
        screen_height = 2 * MARGIN + grid_height   
        Box((0, screen_height), screen_width, screen_height, True, color.GRAY)     
        Text("Chomp",(screen_width/2, screen_height + GRID_SIZE), "#99E5E5", int(GRID_SIZE*1.3))
    def make_object(self, point, character):
        (x, y) = point
        if character == '%':                    # Is it a wall?
            self.map[y][x] = Wall(self, point)
    def finished(self):
        return self.game_over        # Stop if game is over

    def play(self):
        update_when('next_tick')     # Just pass time at loop rate

    def done(self):
        end_graphics()               # We've finished
        self.map = []                       
the_maze = Maze()                 

while not the_maze.finished():    
    the_maze.play()

the_maze.done() 