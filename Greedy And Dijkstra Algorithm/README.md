# Code from 02-26-2025 Code With Me Algorithms Night

Folder Structure:
- /problems contains the starting code for the presentation
- /solution has the solution if needed
- /images has the images for the rendering
- /maps has the map csv for rendering

Files:
- algo.py has the BFS and Dijkstra's algorithms implemented with a hook into the vizualizer
- grid.py main pygame file with visualizer and rendering as well as input handling

## To install using venv on Windows

```
python -m venv .venv
.venv\Scripts\Activate
pip install -r requirements.txt
python grid.py
```

### Grid keyboard commands
| Key | Use |
| :-- | :-- |
| ENTER | cycle to next map |
| N | Show the distance on the map from start to that cell |
| A | Toggle Visualization on/off |
| SPACE | Reset Visualization |
| TAB | Pause Visualzation |
| UP ARROW | Increase the time between frames (moves slower) |
| DOWN ARROW | Reduce the time between frames (moves faster) |
| LEFT ARROW | Go back one frame |
| RIGHT ARROW | Go forward one frame |