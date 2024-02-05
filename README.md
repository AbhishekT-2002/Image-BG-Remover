# Image Background Remover

## Overview

**Image Background Remover** is a straightforward Python script designed to remove backgrounds from images. The script utilizes the `rembg` library, providing a user-friendly command-line interface to remove backgrounds from specific images or all images in a directory.

## Features

- **Welcome Screen:** Displays a simple ASCII art welcome screen using the `pyfiglet` library.
- **Menu Options:**
  - **Show List of Images:** Lists images in the same directory for the user to choose for background removal.
  - **Enter Custom Path:** Allows the user to input the full path to the image file for background removal.
  - **Exit:** Exits the application after confirmation.

## Prerequisites

- Python 3.x
- `rembg` library
- `pyfiglet` library
- `Pillow` library (PIL fork)

## Usage

1. Run the script.
2. Choose an option from the menu.
3. Follow the prompts to either select an image or input a custom path.
4. Background removal is applied using `rembg`.
5. Processed images are saved in the same directory.

## Installation

Install required libraries using:

```bash
pip install rembg pyfiglet Pillow
```

## How to Run

```bash
python script_name.py
```

## Disclaimer

This script is provided as-is without any warranty. Use it responsibly and respect the terms of service of third-party libraries used.

---

**Note:** Press Enter to continue after each operation.

**Thank you for using the Image Background Remover!**
