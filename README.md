# hotkey-typer
a simple script to type predefined text using a customizable hotkey combination


# Hotkey Typer

*A straightforward script that lets you instantly type predefined text snippets using a customizable hotkey.*

## Overview

This project provides a simple way to automate typing repetitive text. It's especially handy for quickly inserting common phrases, commands, or anything you type frequently.

### Features

- **Hotkey Activation:** A specific combination of keys, like the default `Ctrl + Alt + Shift + G`, triggers the text. You can easily change this in the `HOTKEY` variable.
- **Customizable Text:** The actual text that gets typed is defined in the `TEXT_TO_TYPE` variable, which you can modify to be any string you need.

## Setup and Usage

### Installation

Install the required Python libraries:

```bash
pip install pyautogui pynput
```

### Customization

Open the script file.

**Change the Text:** Modify the `TEXT_TO_TYPE` variable:

```python
TEXT_TO_TYPE = "Your custom text here!"
```

**Change the Hotkey (Optional):** Adjust the `HOTKEY` set. For example, to use `Ctrl + Alt + A`:

```python
HOTKEY = {keyboard.Key.ctrl, keyboard.Key.alt, keyboard.KeyCode(char='a')}
```

### Run

Execute the script:

```bash
python your_script_name.py
```

### Activate

With the script running, press your chosen hotkey combination wherever you want the text to appear.

### Exit

Press the `Esc` key to stop the script.
