import pygame
import sys
from algo import bfs, djikstra
import os

FONT_SIZE = 14

LAND = (0, 255, 0)     
WATER = (0, 0, 255)    
LAVA = (255, 0, 0)     
PATH = (128, 128, 128) 
STONE = (45, 45, 45)   
WALL = (15, 15, 15) 
END = (112, 108, 48)
START = (255, 255, 10)

class Vizualizer:
    def __init__(self):
        self.frames = []
        self.i = 0
        self.ticks = 0
        self.delay = 200
        self.pause = False

    def toggle_pause(self):
        self.pause = not self.pause

    def add_delay(self, val):
        self.delay += val
        self.delay = max(0, self.delay)

    def reset(self):
        self.i = 0
        self.ticks = pygame.time.get_ticks()

    def skip_frame(self, val):
        self.i += val
        if self.i < 0:
            self.i == 0
        if self.i >= len(self.frames):
            self.i = len(self.frames) - 1

    def add_frame(self, distance, location, path, state, dist):
        self.frames.append((distance, location, path, state.copy(), dist.copy()))

    def render(self, renderer, offset):
        now = pygame.time.get_ticks()
        if not self.pause and (not self.ticks or now - self.ticks > self.delay):
            self.i = min(self.i + 1, len(self.frames)-1)
            self.ticks = now
        distance, location, path, Q, dist = self.frames[self.i]        
        looking_at = {q[1]: True for q in Q}
        renderer.render_frame(offset, path, dist, location, looking_at)

class Grid:
    NEIGHBORS_4 = [ (1,0), (0,1), (-1, 0), (0, -1)]
    NEIGHBORS_8 = [ (1,0), (1,1), (0,1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1,-1)]

    ID_TO_TYPE = {
        '0': LAND,
        '1': WATER,
        '2': LAVA,
        '3': PATH,
        '4': STONE,
        '5': WALL,
        '6': START,
        '7': END
    }

    COST_TO_TRAVEL = {
        LAND: 1,
        WATER: 23,
        LAVA: 50,
        STONE: 1,
        PATH: 1,
        WALL: 5000,
        START: 1,
        END: 1
    }

    def __init__(self, file=None):
        assert file, "Must specify a file"
        self.load_grid(file)
        self.movement_scheme = Grid.NEIGHBORS_4
        self.prev_start_tile = LAND if file in ["island.csv", "volcano.csv"] else STONE
        self.prev_end_tile = LAND if file in ["island.csv", "volcano.csv"] else STONE

    def load_grid(self, filename):
        self.grid = []
        with open(filename) as file:
            for y, line in enumerate(file.readlines()):
                row = []
                for x, ch in enumerate(line.strip().split(",")):
                    row.append(Grid.ID_TO_TYPE[ch])
                    if ch == '7':
                        self.end = (x,y)
                    elif ch == '6':
                        self.start = (x,y)
                self.grid.append(row)
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def get_neighbors(self, loc):
        results = []        
        x,y = loc
        for offset in self.movement_scheme:
            dx, dy = offset
            new_x = x + dx
            new_y = y + dy

            if 0 <= new_x < self.width and 0 <= new_y < self.height and self.is_passable((new_x, new_y)):
                results.append(((new_x, new_y), Grid.COST_TO_TRAVEL[self.grid[new_y][new_x]]))
        return results
    
    def is_passable(self, loc):
        return self.grid[loc[1]][loc[0]] != WALL

    def set_new_start(self, loc):
        print("new start", loc)
        if loc != self.start:
            tmp = self.prev_start_tile
            self.prev_start_tile = self.grid[loc[1]][loc[0]]
            self.grid[self.start[1]][self.start[0]] = tmp
            self.grid[loc[1]][loc[0]] = START
            self.start = loc

    def set_new_end(self, loc):
        print("new end", loc)
        if loc != self.end:
            tmp = self.prev_end_tile
            self.prev_end_tile = self.grid[loc[1]][loc[0]]
            self.grid[self.end[1]][self.end[0]] = tmp
            self.grid[loc[1]][loc[0]] = END
            self.end = loc

class RenderState:
    def __init__(self):
        self.grid = None
        self.screen = None
        self.window_size = None

        # BFS info
        self.bfs_viz = None
        self.bfs_path = None
        self.bfs_dist = None

        # Dijkstra's info
        self.djk_viz = None
        self.djk_path = None
        self.djk_dist = None

        # Size of each drawn grid cell
        self.cell_size = 50

        self.vizualizer_on = False
        self.show_distance_numbers = False

        self.start_image = pygame.image.load(os.path.join("images", "indy.png"))
        self.end_image = pygame.image.load(os.path.join("images", "chest.png"))

        self.left, self.middle, self.right = False, False, False
        self.mouse_click_position = (-1, -1)

    def reset_mouse(self):
        self.left, self.middle, self.right = False, False, False
        self.mouse_click_position = (-1, -1)

    def load_map(self, file_name):
        self.grid = Grid(file_name)
        self.window_size = (self.grid .width * self.cell_size * 2 + 5, self.grid .height * self.cell_size)
        self.screen = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
        self.run_algos()

    def run_algos(self):
        self.bfs_viz = Vizualizer()
        self.bfs_cost, self.bfs_path, self.bfs_dist = bfs(self.grid, self.grid.start, self.grid.end, self.bfs_viz)
        self.djk_viz = Vizualizer()
        self.djk_cost, self.djk_path, self.djk_dist = djikstra(self.grid, self.grid.start, self.grid.end, self.djk_viz)

    def render_answer(self):
        for offset, path, dist in [(0, render.bfs_path, render.bfs_dist), ((render.grid.width * cell_size) + 5, render.djk_path, render.djk_dist)]:
            self.render_frame(offset, path, dist)

    def render_frame(self, offset, path, dist, location=None, looking_at={}):
        # Draw the grid
        BORDER = 10
        SHRINKAGE = cell_size // 4
        for i in range(render.grid.height):
            for j in range(render.grid.width):
                # Calculate the x and y coordinates of the cell
                x = (j * cell_size) + offset
                y = (i * cell_size)

                if x <= self.mouse_click_position[0] <= x + render.cell_size and y <= self.mouse_click_position[1] <= y + render.cell_size and render.grid.is_passable((j,i)):
                    if self.right:
                        render.grid.set_new_end((j,i))
                    elif self.left:
                        render.grid.set_new_start((j,i))
                    self.run_algos()
                    self.reset_mouse()
                if (j,i) == location:
                    pygame.draw.rect(self.screen, (255, 255, 255), (x, y, cell_size, cell_size))
                    pygame.draw.rect(self.screen, (128, 128, 128), (x+BORDER, y+BORDER, cell_size-2*BORDER, cell_size-2*BORDER))
                elif (j,i) in looking_at:
                    pygame.draw.rect(self.screen, (140, 140, 140), (x, y, cell_size, cell_size))
                    pygame.draw.rect(self.screen, (40, 40, 40), (x+BORDER, y+BORDER, cell_size-2*BORDER, cell_size-2*BORDER))
                elif (j,i) == self.grid.start:
                    self.screen.blit(self.start_image, (x,y))
                elif (j,i) == self.grid.end:
                    self.screen.blit(self.end_image, (x,y))
                else:
                    # Draw cell
                    pygame.draw.rect(render.screen, render.grid.grid[i][j], (x, y, cell_size, cell_size))
                    # Add a path coloring ontop if it's part of the path
                    if (j,i) in path:
                            pygame.draw.rect(render.screen, PATH, (x+SHRINKAGE, y+SHRINKAGE, cell_size-SHRINKAGE*2, cell_size-SHRINKAGE*2))
                
                if render.show_distance_numbers and 0 < dist[(j,i)] < 1e5:
                    pygame.draw.rect(self.screen, (0,0,0), (x+3,y+3,len(str(dist[(j,i)]))*FONT_SIZE, FONT_SIZE+2))
                    font.render_to(render.screen, (x+6-1,y+6-1), str(dist[(j,i)]), (0, 0, 0))
                    font.render_to(render.screen, (x+6,y+6), str(dist[(j,i)]), (255, 255, 255))

            # Titles
            for text, x, y, w in [("BFS", 50, 10, 34), ("Dijkstra's Algo", self.window_size[0] - 180, 10, 134)]:
                pygame.draw.rect(self.screen, (0,0,0), (x,y,w, FONT_SIZE+8))
                font.render_to(render.screen, (x+6-1,y+6-1), str(text), (0, 0, 0))
                font.render_to(render.screen, (x+6,y+6), str(text), (255, 255, 255))

    def render_animated_visualization(self):
        self.bfs_viz.render(self, 0)
        self.djk_viz.render(self, (self.grid.width * self.cell_size) + 5)

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Code With Me Algorithms Night")

# Init fonts
pygame.font.init()
font = pygame.freetype.SysFont('Consolas', FONT_SIZE)

# This is the list of maps we can show and cycle through
maps = [ os.path.join("maps", file) for file in ["maze.csv", "maze2.csv", "maze_water.csv", "cwm.csv",  "island.csv", "volcano.csv" ]]
current_map_index = 0

cell_size = 50
render = RenderState()
render.load_map(maps[current_map_index])

# Main loop
while True:

    # Handle the events of the system so we can interact with the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            render.left, render.middle, render.right = pygame.mouse.get_pressed()
            render.mouse_click_position = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            render.mouse_click_position = pygame.mouse.get_pos()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                render.vizualizer_on = not render.vizualizer_on
            elif event.key == pygame.K_SPACE:
                render.bfs_viz.reset()
                render.djk_viz.reset()
            elif event.key == pygame.K_UP:
                render.bfs_viz.add_delay(100)
                render.djk_viz.add_delay(100)
            elif event.key == pygame.K_DOWN:
                render.bfs_viz.add_delay(-100)
                render.djk_viz.add_delay(-100)
            elif event.key == pygame.K_TAB:
                render.bfs_viz.toggle_pause()
                render.djk_viz.toggle_pause()
            elif event.key == pygame.K_LEFT:
                render.bfs_viz.skip_frame(-1)
                render.djk_viz.skip_frame(-1)
            elif event.key == pygame.K_RIGHT:
                render.bfs_viz.skip_frame(1)
                render.djk_viz.skip_frame(1)                
            elif event.key == pygame.K_n:
                render.show_distance_numbers = not render.show_distance_numbers
            elif event.key == pygame.K_RETURN:
                current_map_index += 1
                current_map_index %= len(maps)
                render.load_map(maps[current_map_index])
            elif event.key == pygame.K_8:
                render.grid.movement_scheme = Grid.NEIGHBORS_8
            elif event.key == pygame.K_4:
                render.grid.movement_scheme = Grid.NEIGHBORS_4

    render.screen.fill((0, 0, 0))
    if not render.vizualizer_on:
        render.render_answer()
    else:
        render.render_animated_visualization()

    pygame.display.update()