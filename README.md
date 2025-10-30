<h1 align="center">🟡 Pac-Man AI Game</h1>

<p align="center">
  <b>A modern Python remake of the classic Pac-Man — powered by Pygame and A* pathfinding AI.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Pygame-2.0%2B-green?logo=pygame" alt="Pygame">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
</p>



# 🟡 Pac-Man AI Game

A modern Python implementation of the **classic Pac-Man**, built using **Pygame**.  
Includes **AI-controlled ghosts** powered by the **A* pathfinding algorithm** for realistic chasing behavior.

---

## 🎮 Features

- Playable Pac-Man with smooth grid-based movement  
- Four ghost enemies with different colors and behaviors  
- A* pathfinding logic for intelligent ghost chasing  
- Interactive home/start screen with animations  
- Score tracking and win/lose conditions  
- Clean UI with restart option

---

## 🧩 Project Structure

```
pacman-ai-game/
│
├── main.py             # Entry point (runs the whole game)
├── home_screen.py      # Start menu with animated ghosts and Start button
├── game.py             # Main game logic (score, collisions, state)
├── pacman.py           # Pac-Man movement and rendering
├── ghost.py            # AI ghosts with A* pathfinding
├── astar.py            # A* algorithm for ghost movement
├── maze.py             # Maze structure and dots generation
├── utils.py            # Utility functions for grid-pixel conversion
├── setting.py          # Constants like colors and screen size

```
