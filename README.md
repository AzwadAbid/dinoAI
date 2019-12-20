# dinoAI
CNN trained to play Google's dinosaur run game.

*The Code is cleaned up for use with Windows 10. Thanks to Fisher for writing the program*

Prerequisites:
1. Download Chromedriver from their official website.
https://sites.google.com/a/chromium.org/chromedriver/home

2. Extract and place "chromedriver.exe" in your root folder.

## FILE DESCRIPTION

### Step 1 | capture_training_data.py

Start game and capture training data, frame and respective action (do nothing, jump, duck). Writes these actions to actions.csv and frames to images folder.

### Step 2 | network.py

Train CNN on captured data.
I changed batch_size to 20 as my GPU cannot take very big batches. You can train with higher batches if you have a good GPU with larger memory size.

### Step 3 | play_game.py

Open and play game with trained network.
