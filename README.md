## IQ Twist
This is a game solving project for the logic game called IQ Twist where you have to fit pieces into a frame keeping in mind certain constraints like coloured pins.

It's a really fun game, you can buy it [here](https://www.smartgames.eu/uk/one-player-games/iq-twist), it's perfect for Christmas.
It's a really fun game, you can buy it [here](https://www.smartgames.eu/uk/one-player-games/iq-twist), it's perfect for Christmas.
<div align="center">
  <a href="https://www.smartgames.eu/uk/one-player-games/iq-twist">
    <img src="images/iqtwist_img.png" alt="iqLogo" width="400" height="225">
  </a>
</div>

> [!NOTE]  
> This is not an illegal copy of the game, you cannot move around the pieces and such, it is only meant to implement the algorithm, and display the result in the end.

### Prerequisites

You will need to install [python](https://www.python.org/downloads/) and the pygame package, only for visualization.
* To install pygame just use pip
  ```sh
  pip install pygame
  ```
### Instructions
To use the program, you have to add the initial pieces and pins to the board in the main.py file as lists, then run it.
For example if you want to add a red pin to position '6B' and a greeen pin to '3C', type
```python
exerciseSetup_pins = ['R6B','G3C']
```
and for the green piece with 4 blocks, with rotation 6 and with the top left block being at '4C', type
```python
exerciseSetup_pieces = [['Green4',6,(2,3)]]
```

### Rotations
<img src="images/screenshot.png" alt="Piece" width="600" height="600">
<!-- <table>
  <tr>
    <th></th>
    <th>0</th>
    <th>1</th>
    <th>2</th>
    <th>3</th>
    <th>4</th>
    <th>5</th>
    <th>6</th>
    <th>7</th>
  </tr>
  <tr>
    <td>RedL</td>
    <td><img src="images/RedL.png" alt="Piece" width="60" height="40"></td>
    <td><img src="images/RedL.png" alt="Piece" width="60" height="40" style="transform: rotate(-90deg);"></td>
    <td><img src="images/RedL.png" alt="Piece" width="60" height="40" style="transform: rotate(-180deg);"></td>
    <td><img src="images/RedL.png" alt="Piece" width="60" height="40" style="transform: rotate(-270deg);"></td>
    <td><img src="images/RedL.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1);"></td>
    <td><img src="images/RedL.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(90deg); "></td>
    <td><img src="images/RedL.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(180deg); "></td>
    <td><img src="images/RedL.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(270deg); "></td>
  </tr>
  <tr>
    <td>RedZ</td>
    <td><img src="images/RedZ.png" alt="Piece" width="60" height="40"></td>
    <td><img src="images/RedZ.png" alt="Piece" width="60" height="40" style="transform: rotate(-90deg);"></td>
    <td><img src="images/RedZ.png" alt="Piece" width="60" height="40" style="transform: rotate(-180deg);"></td>
    <td><img src="images/RedZ.png" alt="Piece" width="60" height="40" style="transform: rotate(-270deg);"></td>
    <td><img src="images/RedZ.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1);"></td>
    <td><img src="images/RedZ.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(90deg); "></td>
    <td><img src="images/RedZ.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(180deg); "></td>
    <td><img src="images/RedZ.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(270deg); "></td>
  </tr>
  <tr>
    <td>Green3</td>
    <td><img src="images/Green3.png" alt="Piece" width="40" height="40"></td>
    <td><img src="images/Green3.png" alt="Piece" width="40" height="40" style="transform: rotate(-90deg);"></td>
    <td><img src="images/Green3.png" alt="Piece" width="40" height="40" style="transform: rotate(-180deg);"></td>
    <td><img src="images/Green3.png" alt="Piece" width="40" height="40" style="transform: rotate(-270deg);"></td>
    <td><img src="images/Green3.png" alt="Piece" width="40" height="40" style="transform: scaleX(-1);"></td>
    <td><img src="images/Green3.png" alt="Piece" width="40" height="40" style="transform: scaleX(-1) rotate(90deg); "></td>
    <td><img src="images/Green3.png" alt="Piece" width="40" height="40" style="transform: scaleX(-1) rotate(180deg); "></td>
    <td><img src="images/Green3.png" alt="Piece" width="40" height="40" style="transform: scaleX(-1) rotate(270deg); "></td>
  </tr>
  <tr>
    <td>Green4</td>
    <td><img src="images/Green4.png" alt="Piece" width="60" height="40"></td>
    <td><img src="images/Green4.png" alt="Piece" width="60" height="40" style="transform: rotate(-90deg);"></td>
    <td><img src="images/Green4.png" alt="Piece" width="60" height="40" style="transform: rotate(-180deg);"></td>
    <td><img src="images/Green4.png" alt="Piece" width="60" height="40" style="transform: rotate(-270deg);"></td>
    <td><img src="images/Green4.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1);"></td>
    <td><img src="images/Green4.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(90deg); "></td>
    <td><img src="images/Green4.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(180deg); "></td>
    <td><img src="images/Green4.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(270deg); "></td>
  </tr>
  <tr>
    <td>Blue4</td>
    <td><img src="images/Blue4.png" alt="Piece" width="80" height="20"></td>
    <td><img src="images/Blue4.png" alt="Piece" width="80" height="20" style="transform: rotate(-90deg);"></td>
    <td><img src="images/Blue4.png" alt="Piece" width="80" height="20" style="transform: rotate(-180deg);"></td>
    <td><img src="images/Blue4.png" alt="Piece" width="80" height="20" style="transform: rotate(-270deg);"></td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Blue5</td>
    <td><img src="images/Blue5.png" alt="Piece" width="60" height="40"></td>
    <td><img src="images/Blue5.png" alt="Piece" width="60" height="40" style="transform: rotate(-90deg);"></td>
    <td><img src="images/Blue5.png" alt="Piece" width="60" height="40" style="transform: rotate(-180deg);"></td>
    <td><img src="images/Blue5.png" alt="Piece" width="60" height="40" style="transform: rotate(-270deg);"></td>
    <td><img src="images/Blue5.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1);"></td>
    <td><img src="images/Blue5.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(90deg); "></td>
    <td><img src="images/Blue5.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(180deg); "></td>
    <td><img src="images/Blue5.png" alt="Piece" width="60" height="40" style="transform: scaleX(-1) rotate(270deg); "></td>
  </tr>
  <tr>
    <td>Yellow3</td>
    <td><img src="images/Yellow3.png" alt="Piece" width="60" height="20"></td>
    <td><img src="images/Yellow3.png" alt="Piece" width="60" height="20" style="transform: rotate(-90deg);"></td>
    <td><img src="images/Yellow3.png" alt="Piece" width="60" height="20" style="transform: rotate(-180deg);"></td>
    <td><img src="images/Yellow3.png" alt="Piece" width="60" height="20" style="transform: rotate(-270deg);"></td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
    <td>-</td>
  </tr>
  <tr>
    <td>Yellow5</td>
    <td><img src="images/Yellow5.png" alt="Piece" width="60" height="60"></td>
    <td><img src="images/Yellow5.png" alt="Piece" width="60" height="60" style="transform: rotate(-90deg);"></td>
    <td><img src="images/Yellow5.png" alt="Piece" width="60" height="60" style="transform: rotate(-180deg);"></td>
    <td><img src="images/Yellow5.png" alt="Piece" width="60" height="60" style="transform: rotate(-270deg);"></td>
    <td><img src="images/Yellow5.png" alt="Piece" width="60" height="60" style="transform: scaleX(-1);"></td>
    <td><img src="images/Yellow5.png" alt="Piece" width="60" height="60" style="transform: scaleX(-1) rotate(90deg); "></td>
    <td><img src="images/Yellow5.png" alt="Piece" width="60" height="60" style="transform: scaleX(-1) rotate(180deg); "></td>
    <td><img src="images/Yellow5.png" alt="Piece" width="60" height="60" style="transform: scaleX(-1) rotate(270deg); "></td>
  </tr>
</table> -->
