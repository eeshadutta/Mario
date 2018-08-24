# OBJECTTIVE
The objective of the game is to reach the flag before the 100 seconds of the game are up.

# RUNNING THE GAME
```
pip3 install -r requirements.txt
python3 main.py
```

# FEATURES
- The game is implemented in Python3
- The code is modular and follows PEP8 standards
- Uses only core Python3 packages
- Player can move right, left and jump
- Smart enemies which follow the player and move faster when farther away from the player
- Colors are implemented
- Sound (on jump, enemy kill, bonus collection)

# MOVEMENT
- a - Move Backwards
- d - Move forward
- j - Jump vertical (to jump in a particular direction, use the apropriate key, a or d during the jump)

# OOP
- #### Inheritance
    - Player and Enemy class inherit from the Person class
    - All the obstcles like Bricks, Pipes, Holes and scenery like Cloud, Hills inherit from the Obstacle class
- #### Polymorphism
   - The draw function in each of the child classes of the Obstacle class overrides the draw function of the Obstacle class
- #### Encapsulation
    - Class and object based approach for all the functionality implemented
- #### Abstraction
    - Properties of the board class are hidden from the user using abstraction

# OBSTACLES
- Bricks, Pipes, Bridges, Holes are the various obstacles implemented

# BACKGROUND AND SCENERY
- The scenery changes when the player moves forward beyond a certain limit

# SCORE
- The final score is calculated as:
```
final score = 100 * (number of enemy kills) + 100 * (number of coins collected) + 50 * (time left)
```