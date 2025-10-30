# DESIGN.md

# Design Documentation for Krunker Style 3D Game

## Overview
This document outlines the design philosophy, architecture, and visual style of the Krunker Style 3D game project. The game features two main character classes: "Assaltantes" and "Policiais," each with male and female skins. The game aims to provide an engaging multiplayer experience with fast-paced action and visually appealing graphics.

## Game Architecture
The game is structured into several key components:

1. **Game Engine**: The core of the game, responsible for rendering, physics, and input handling. This is implemented in `engine.py`.

2. **Game Logic**: The main game loop and state management are handled in `game.py`. This includes event handling and game state transitions.

3. **Asset Management**: All game assets, including models, textures, and audio, are loaded and managed by `assets_loader.py`.

4. **Player Class**: The player attributes and actions are defined in `player.py`, allowing for character movement and interaction.

5. **Weapon Class**: The weapon handling, including attributes and methods for different weapon types, is defined in `weapon.py`.

6. **User Interface**: The UI elements, including menus and HUD, are managed in `ui.py`.

7. **Character Classes**: The "Assaltantes" and "Policiais" classes are defined in separate files, encapsulating their unique properties and behaviors.

## Visual Style
The game adopts a modern, stylized aesthetic reminiscent of popular first-person shooters. Key visual elements include:

- **3D Models**: High-quality models for characters and weapons, designed to be visually appealing and optimized for performance.
- **Textures**: Detailed textures for characters and environments, enhancing the overall visual fidelity.
- **Shaders**: Custom shaders to achieve dynamic lighting and effects, contributing to a more immersive experience.

## Character Design
### Assaltantes
- **Male Skins**: Robust and agile designs, featuring tactical gear and urban clothing.
- **Female Skins**: Sleek and stealthy designs, incorporating modern fashion elements suitable for combat.

### Policiais
- **Male Skins**: Traditional police uniforms with tactical enhancements, emphasizing authority and strength.
- **Female Skins**: Professional and functional designs, maintaining a balance between style and practicality.

## Gameplay Features
- **Multiplayer Support**: The game is designed for online multiplayer, allowing players to engage in team-based combat.
- **Weapon Variety**: A range of weapons, including rifles, pistols, and melee options, each with unique handling and characteristics.
- **Dynamic Environments**: Interactive environments that enhance gameplay, providing cover and strategic advantages.

## Conclusion
This design document serves as a foundation for the development of the Krunker Style 3D game. It outlines the key components, visual style, character design, and gameplay features that will guide the project towards a successful implementation.