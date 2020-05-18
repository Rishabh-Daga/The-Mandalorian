# The Mandalorian
A terminal based game coded in ```python3``` which is inspired from the famous game Jetpack Joyride.

## About the Game
The game follows Mando, who tries to rescue Baby Yoda from an evil dragon. But, it's not easy to reach the dragon, and even if you reach the dragon, it is very difficult to defeat the bullet firing dragon.

## Game Feature
1. Lots of coins suspended throughout the game for Mando to collect.
2. Beams appear as obstacles. If Mando collides with a beam, he loses a life.
3. Shield which becomes active after 30 seconds and remains active for 10 seconds or until Mando hits a beam or is hit by a bullet.
4. A Magnet which attracts Mando towards itself.
5. Boss Dragon which fires balls towards Mando to kill him. The Boss has 10 lives, same as Mando.
6. Game Time: Player gets 75 seconds to kill the Boss Dragon and rescue Baby Yoda
7. Bullets: Mando is equipped with bullets which he can use to destroy obstacles and kill the Boss Dragon.

## Controls
1. W - move up
2. D - move right
3. A - move left
4. S - move down
5. F - fire bullet

## How to Run the Game
1. First, we need to install the dependencies for the game. Do so by running the following command:
``` sudo pip3 install -r requirements.txt```
2. Now, we can play the game by simply running the command:
``` python3 jetpack.py```