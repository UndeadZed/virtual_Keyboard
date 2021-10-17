# virtual_Keyboard
this is a lite easy to use virtual keyboard project for anyone to use

# How to use:

## Step 1: 

I recommend that you setup a virtual environment using anaconda or python venv

```python
conda create -n env_name python=3.6
```

## Step 2:

activate the environment using the following command

```python
conda activate env_name
```

## Step 3:

you should clone the repository if you haven't already using the following command or just by installing the project directly

```python
git clone https://github.com/UndeadZed/virtual_Keyboard
```

## Step 4:

install the requirements from the [requirements.txt file](https://github.com/UndeadZed/virtual_Keyboard/blob/main/requirements.txt) by typing the following command in the terminal

```python
pip install -r requirements.txt
```

## Step 5:

now we're done with the setup you can now use the virtual keyboard by typing this command in the terminal

```python
python keyboard.py
```

# Some notes about the keyboard:

## these are the points that the hand tracking actually tracks

![Mediapipe hand tracking](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png)

A button is selected when the point number 8 is in the same location which is shown by the button getting visibly darker but in order to register a button press you should connect your thumb with your index finger basically connecting point 8 with point 4 which would make this gesture for obvious reasons


![Button press gesture](https://bostonglobe-prod.cdn.arcpublishing.com/resizer/fdHfgp51LzfrOwfP1mtQw0iAD88=/1440x0/arc-anglerfish-arc2-prod-bostonglobe.s3.amazonaws.com/public/UJPHCNAIXEI6NLRQD4MDZH4XQA.jpg)



