# Catch the Egg Game

This is a simple arcade-type game called "Catch the Egg" implemented in Python using the Tkinter library. The objective of the game is to catch falling eggs with a catcher controlled by the player. Each caught egg adds points to the score, while missing an egg results in losing a life. The game continues until all lives are exhausted.

## Installation

To run the game, make sure you have Python installed on your system. The game utilizes the Tkinter library, which is usually included with Python distributions.

1. Clone the repository or download the source code file.

2. Open a terminal or command prompt and navigate to the directory containing the source code.

3. Run the following command to start the game:

   ```bash
   python catch_the_egg.py
   ```

## How to Play

1. After launching the game, a window will appear with a catcher at the bottom and eggs falling from the top.

2. Move the catcher left and right using the left and right arrow keys on your keyboard, respectively. The objective is to position the catcher under the falling eggs to catch them.

3. Each caught egg will add 10 points to your score. Missing an egg will deduct one life.

4. The game ends when all lives are exhausted. A dialog box will appear showing your final score.

## Game Mechanics

### Game Elements

- **Canvas**: The game window where the gameplay takes place. It has a blue background with a green ground at the bottom.

- **Eggs**: Oval-shaped objects that fall from the top of the canvas. Each egg has a random color and falls at a certain speed. The eggs are randomly generated at intervals of 4 seconds.

- **Catcher**: An arc-shaped object controlled by the player. The catcher moves horizontally to catch the falling eggs.

- **Score**: Displays the current score of the player.

- **Lives**: Shows the number of remaining lives.

### Game Flow

1. The game initializes by creating the game window, setting up the canvas, and defining initial game parameters such as egg speed, egg interval, and difficulty factor.

2. The game continuously generates eggs at regular intervals using the `create_egg()` function.

3. The eggs start falling from the top of the canvas and move down at a specified speed. The `move_eggs()` function handles the movement of eggs.

4. The `check_catch()` function checks if any falling eggs are caught by the catcher. If an egg is caught, it is removed from the canvas, and the player's score is increased.

5. If an egg reaches the bottom of the canvas without being caught, the `egg_dropped()` function is called. It removes the egg from the canvas, deducts a life, and checks if the game is over.

6. The player can move the catcher left and right using the arrow keys. The `move_left()` and `move_right()` functions handle the catcher's movement.

7. The game continues until all lives are exhausted. When this happens, a dialog box appears showing the player's final score.

## Customization

The game can be customized by modifying the following variables:

- `canvas_width` and `canvas_height`: Adjust the dimensions of the game window.

- `egg_width` and `egg_height`: Change the size of the eggs.

- `egg_score`: Modify the score value obtained for catching each egg.

- `egg_speed`: Adjust the speed at which eggs fall.

- `egg_interval`: Change the time interval between generating new eggs.

- `difficulty_factor`: Adjust the rate at which the game difficulty increases after each catch.

- `catcher_color`: Change the color of the catcher.

- `catcher_width` and `catcher_height`:

 Adjust the size of the catcher.
 
 
 ## Contributing

Contributions are welcome! Here are some guidelines on how you can contribute to the project:

1. Fork the repository on GitHub.
2. Create a new branch from the main branch to work on your changes.
3. Make the necessary modifications and improvements to the codebase.
4. Write tests to ensure the stability and correctness of your changes.
5. Commit your changes and push them to your forked repository.
6. Open a pull request against the main repository, describing your changes in detail.

Please ensure that your contributions align with the following guidelines:

- Follow the existing coding style and conventions used in the project.
- Write clear and concise commit messages and provide an informative description in your pull request.
- Test your changes thoroughly and ensure they do not introduce any regressions.
- Provide proper documentation and comments to help others understand your contributions.

Thank you for your interest in contributing to this project! Your contributions will be greatly appreciated.


## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and distribute the code according to the terms of the license.