# Catch The Egg - Release Notes

## Version 1.0.0

This is the initial release of Catch The Egg, an arcade-style game implemented in Python using the Tkinter library. The game involves catching falling eggs with a catcher controlled by the player. Each caught egg increases the score, while missing an egg results in losing a life. The game continues until all lives are exhausted.

### Features

- Falling Eggs: Oval-shaped objects fall from the top of the game window.
- Catcher: An arc-shaped object controlled by the player to catch the falling eggs.
- Score: Displays the current score of the player.
- Lives: Shows the number of remaining lives.
- Game Over: The game ends when all lives are exhausted, and a dialog box displays the final score.

### Instructions

To run the game, make sure you have Python installed on your system. The game utilizes the Tkinter library, which is usually included with Python distributions.

1. Clone the repository or download the source code file.
2. Open a terminal or command prompt and navigate to the directory containing the source code.
3. Run the following command to start the game:
   ```bash
   python catch_the_egg.py
   ```

### Customization

You can customize certain aspects of the game by modifying the following variables in the source code:

- `canvas_width` and `canvas_height`: Adjust the dimensions of the game window.
- `egg_width` and `egg_height`: Change the size of the eggs.
- `egg_score`: Modify the score value obtained for catching each egg.
- `egg_speed`: Adjust the speed at which eggs fall.
- `egg_interval`: Change the time interval between generating new eggs.
- `difficulty_factor`: Adjust the rate at which the game difficulty increases after each catch.
- `catcher_color`: Change the color of the catcher.
- `catcher_width` and `catcher_height`: Adjust the size of the catcher.

### License

This project is licensed under the MIT License. Feel free to modify and distribute the code according to the terms of the license.

For more details, refer to the [LICENSE](LICENSE) file.

---

Thank you for trying out Catch The Egg! We hope you enjoy playing the game. If you encounter any issues or have any feedback, please don't hesitate to [create an issue](https://github.com/Sagarmishra-C30/Catch-the-Egg/issues) on the project's GitHub repository.