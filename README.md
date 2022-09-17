# Gravkitty


Overview and Target Audience:
  The final product of this project is a simple platformer game called Gravkitty. The main unique feature of this game compared to 
  other platformers is that instead of a jump mechanic, there is a gravity switch mechanic, in which the direction of gravity will switch, 
  making the player alternate between walking on the ceiling and walking on the ground. Since Gravkitty is a video game, or in other words, 
  an entertainment item, the problem that it is a solution to is one of boredom. In theory, Gravkitty is meant for people who feel like playing 
  a quick platforming game. The game is very straightforward, and can be enjoyed by people of all ages due to the simplicity of the controls 
  and the intentional use of graphic design to make the goal of the game clear (the end goal being a flag, etc.). The level of technical expertise
  to use Gravkitty is very low, as someone just needs to be able to use a computer enough to open the file. Finally, in theory, the motivation 
  of someone using Gravkitty is to have fun, but realistically it will be mostly used by my friends and acquaintances as a way for me to
  update them on how much progress I’ve made in learning how to program. 


Features and Functionality:
  The final product of Gravkitty contains the following features and functions:
  Four game states:
    Title screen that appears upon start up and after game over/game won states
    Game state: Map with starting point on the left and ending point on the right. Contains ground and ceiling platforms between which the player can switch. 
        Includes three types of obstacles that lead to the game over state upon collision.
    Game over state: Displays game over message, leads back to title screen
    Game won state: Displays game won message, leads back to title screen
  Obstacles:
  Black hole: Static obstacle floating between floor and ceiling platforms
  Spikes: Static obstacle on ground and ceiling
  Laser: Intermittently firing obstacle that must be passed through to reach end point
  Art design:
    Player character is a sprite of a cat
    Obstacle sprites correspond to the objects they are depicting
    Ending point is a sprite of a flag
    Title, game over, and game won screens contain starry background and appropriate text
    Title screen contains pixel art of a tuxedo cat
  Sound design:
    Sound effect for laser zapping
    Sound effect for game over screen
    Sound effect for game won screen
    Sound effect for gravity switch
    Unique music for title screen
    Unique music for game screen
  Three movement controls:
    Switch gravity
    Move left and right
    Move left and right w/ a dash
  Difficulty: The game is designed to give some level of challenge so that beating it in one try is difficult to do. It requires some precise platforming and timing of dashing to complete. 


Usage Instructions
The following explain how to use the product from start to finish:
1. User launches Gravkitty.exe
2. Press enter on title screen to start game
3. Three in game controls:
     Left/right keys to move left and right
     Hold v while pressing left and right to move faster
     Press space to switch direction of gravity
4. If the player collides with an obstacle, the game over screen will appear. Press space to return to the title screen. 
5. If the player reaches the endpoint flag and collides with it, the game won screen will appear. Press space to return to the title screen. 
6. Close the game by pressing the exit button on the top right of the game window. 
