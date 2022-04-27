![Logo](assets/images/junkitbox_logo.png)
# JukeItBox
***A little game made with Python and Pygame.***

Navigate your way through falling enemies.

Arrowkeys to control.

![Enemy](assets/images/killer2.png)

---

### How to download and play the game?

**option 1**
- Clone the repository and run JukeItBox.py with python.

**option 2**
- Download [JukeItBox.zip](JukeItBox.zip), unpack it and run JukeItBox.exe
    - Make sure you have the 'assets' in the same folder as the .exe file.
    
---

### Changing the settings (inside JukeItBox.py)

|   LINE    |                    CODE                     |                    SETTINGS                    |
| :-------: |  :---------------------------------------:  | :--------------------------------------------: |
|           |                                             |                   **DISPLAY**                  |
|     18    |                `FPS = num`                  |         num = clockspeed of the game           |
|     19    |      `WIN_WIDTH, WIN_HEIGHT = num1, num`    | num1 = width of the screen <br /> num2 = height of the screen |
|           |                                             |                   **VOLUME**                   |
|     29    |         `CLICK_SOUND.set_volume(num)`       |   num = 0.0 - 1.0 <br /> changes button volume |
|     31    |            `MUSIC.set_volume(num)`          |   num = 0.0 - 1.0 <br /> changes music volume  |
|     33    |         `DEATH_SOUND.set_volume(num) `      |   num = 0.0 - 1.0 <br /> changes death volume  |
|           |                                             |                **GAME VARIABLES**              |
|     54    |              `VELOCITY = num`               |                num = player speed              |
|     55    |          `ENEMY_VELOCITY = num`             |                num = enemy speed               |
|     57    |           `killer_count = num`              |             num = number of enemies            |

---

### Technicalities
- Progammed with Python.
- The game uses:
    - [Pygame](https://www.pygame.org/news) module library.
    - Python3 [random module](https://docs.python.org/3/library/random.html) for randomising enemy spawns.
    - Python3 [sys module](https://docs.python.org/3/library/sys.html) for closing the program properly.
    - I used [Pyinstaller](https://pyinstaller.org/en/stable/) to build the executable file.
- All the images and sounds are made by myself.
