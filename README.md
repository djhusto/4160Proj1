# 4160Proj1
David Huston-Hakey
CPSC 4160
Dr. Adkins

Program Versions

OS Version : macOS Mojave 10.14.6

Python Version : Python 3.9.12

Pygame Version : pygame 2.1.2

Motivation: I chose pong because it was the first game we spoke about in the class.
It did not seem too confusing and pretty straightforward on how to approach, code, and separate into their appropriate MVC. This seemed to have been an overlook in 
terms of MVC and how I implemented the system. 

Reasoning: I chose to program it all into one file because I prioritized performance over structure. I wanted to create a
working system first then in future iterations of the game to maybe separate the files. I also chose to only have the ball move
after a key was pressed. I am really proud of that particular aspect as I thought it was really cool to have that interaction
with the user.

Known Bugs/Glitches:
1. After a point is scored. The ball continues on the same trajectory once it restarts.
    Fix: On the reset function, speed in both directions gets reset to default
          This should hopefully help with the initial start of the game and the restart of the game after a player has scored
2. Ball gets stuck behind the paddle without points being awarded
    Fix: Im not sure about a fix for this. It is a very sparse bug but it sometimes occurs.
3. There is lag and delay with the ball and paddle movement. This feature is addressed in the Future Improvement Section. 

Future Improvement:
1. Separate the main.py file into separate ball, paddle, view, model, and controller classes. This helps with generalization
and being able to reuse file for future projects.
2. Clock. There is some lag and delay when the ball moves. I think a clock will alleviate some of these issues. Game Time is important. 
3. Colors. I think I could add some more color. The original pong lacked color but Pygame allows for that. 
4. Speed increase upon paddle hit. This was a feature of the original pong game and this would greatly increase the likeness. 


How to Play: Standard Pong Game: Game will not start until a key is pressed
W/S Keys move Left Paddle
Up/Down Arrows move Right Paddle

Generalization:
One important part of generalization for this game is the collision system. Having rectangles be able to interact with eachother 
can be important for future games regarding collisions and block detection. 
