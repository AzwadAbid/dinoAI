# dinoAI
CNN trained to play Google's dinosaur run game.

*The Code is cleaned up for use with Windows 10. Thanks to Fisher for writing the program*

## FILE DESCRIPTION

### capture_training_data.py

Starts game and captures training data, frame and respective action (do nothing, jump, duck). Writes these actions to actions.csv and frames to images folder.

### network.py

Trains CNN on captured data.

### play_game.py

Opens and plays game with trained network. Ensure wifi is off.
