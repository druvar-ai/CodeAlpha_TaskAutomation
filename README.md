# CodeAlpha Task Automation — JPG File Organizer

## Overview
This is a command-line Python automation script created for **CodeAlpha Python Programming Internship Task 3**. It automates a small repetitive real-life task by automatically moving `.jpg` (and `.JPG`) files from a `source` directory to a `destination` directory.

## Features
- **Automated File Organization:** Scans for `.jpg` files in the source directory and moves them.
- **Case-Insensitive Matching:** Correctly identifies both `.jpg` and `.JPG` extensions.
- **Safe Duplicate Handling:** Prevents silent overwriting by skipping files if a file with the same name already exists in the destination folder.
- **Automatic Directory Creation:** Creates the destination directory automatically if it doesn't exist.
- **Clean Error Handling:** Handles missing directories and permission errors with user-friendly messages rather than crashing.

## Technologies
- Python (3.x)
- `pathlib` (for clean, cross-platform path handling)
- `shutil` (for file movement operations)

## How it works
1. **Source directory scanning:** The script checks the local `source` directory for files.
2. **Identification:** It identifies files ending in `.jpg` or `.JPG` while ignoring unrelated files like `.txt` or `.png`.
3. **Destination preparation:** It verifies or creates the `destination` directory.
4. **Execution:** Valid JPG files are moved safely from `source` to `destination`.
5. **Reporting:** A clean summary is printed to the console showing how many files were found, moved, or skipped.

## Requirements
- Python 3.x
- **No external dependencies** (uses only the Python standard library).

## How to run
1. Open your terminal or command prompt.
2. Navigate to the project folder.
3. Run the following command:

```bash
python main.py
```
*(On macOS/Linux, you might need to use `python3 main.py` depending on your environment).*

## How to demonstrate
1. Place any `.jpg` images you want to organize inside the `source/` folder.
2. Run the script as shown above.
3. Check the `destination/` folder to see the successfully moved files.
4. If you run the script again with the same files, it will skip them to prevent overwriting existing files in the destination.

## CodeAlpha Requirement Mapping
- **Automate a repetitive file task** → Implemented (automates moving image files).
- **Move `.jpg` files from one folder to another** → Implemented.
- **Python file handling** → Implemented.
- **`shutil`/filesystem operations** → Implemented via `pathlib` and `shutil.move`.
