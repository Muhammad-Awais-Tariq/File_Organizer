# File Organizer (Automatic Folder Cleaner)
A simple command-line based file organizer that cleans and arranges messy folders by categorizing files into different subfolders based on their extensions.

## Features
- Automatically organizes files into categories (Images, Videos, Documents, etc.)
- Creates a dedicated folder to store all organized files
- Supports a wide range of file types and extensions
- Detects duplicate files (e.g., files with "- Copy" in name)
- Asks user before deleting duplicate files
- Moves all folders into a separate "Folders" directory
- Places unknown file types into a "Miscellaneous" folder
- Simple and interactive command-line interface

## How the Program Works
Run the program and enter the path of the folder you want to organize.

- The program first asks for a name of a new folder where all organized files will be stored.
- It scans all files in the given directory.
- Duplicate files are detected (based on naming like "- Copy") and the user is asked whether to delete them.
- Files are categorized based on their extensions:
  - Images → jpg, png, gif, etc.
  - Videos → mp4, mkv, etc.
  - Documents → pdf, docx, txt, etc.
  - Source Code → py, java, cpp, etc.
  - And many more...
- Each file is moved into its respective category folder.
- Subfolders are moved into a separate "Folders" directory.
- Any file that does not match known extensions is moved to "Miscellaneous".

## How to Run the Program

### Option 1: Using Python (Simple Way)
1. Make sure **Python** is installed.
2. Run the program:
   ```bash
   python main.py
   ```

### Option 2: Using uv (Optional)
1. Install **uv** (if not already installed):
   ```bash
   pip install uv
   ```
2. Sync the project environment:
   ```bash
   uv sync
   ```
3. Run the program:
   ```bash
   uv run main.py
   ```

## File Structure
```bash
project/
│── main.py
│── README.md
│── .gitignore
│── .python-version
│── pyproject.toml
│── uv.lock
```

## Technologies Used
- Python
- os module (for file and directory handling)

## Notes
- The program modifies your files by moving them, so use it carefully.
- Always provide a valid directory path when prompted.
- Duplicate detection is based only on file naming ("- Copy"), not file content.
- If a folder with the chosen name already exists, you will be asked to enter a new name.

## Author
Muhammad Awais Tariq

---
If you like this project, consider giving it a star on GitHub!