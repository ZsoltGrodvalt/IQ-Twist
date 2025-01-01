## IQ Twist
This is a game solving project for the logic game called IQ Twist where you have to fit pieces into a frame keeping in mind certain constraints like coloured pins.

It's a really fun game, you can buy it [here](https://www.smartgames.eu/uk/one-player-games/iq-twist), it's perfect for Christmas.
<div align="center">
  <a href="https://www.smartgames.eu/uk/one-player-games/iq-twist">
    <img src="images/iqtwist_img.png" alt="Logo" width="400" height="200">
  </a>
</div>

### Prerequisites

You will need to install [python](https://www.python.org/downloads/) and the pygame package, only for visualization.
* To install pygame just use pip
  ```sh
  pip install pygame
  ```
### Instructions
To use the program, you have to add the initial pieces and pins to the board in the main.py file, then run it.
For example if you want to add a red pin to position '6B' and a greeen pin to '3C', type
```
exerciseSetup_pins = ['R6B','G3C']
```
and for the green piece with 4 blocks, with rotation 6 and with the top left block being at '4C', type
```
exerciseSetup_pieces = [['Green4',6,(2,3)]]
```

### Rotations
