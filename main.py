import os
import shutil
from pathlib import Path

def main():
    print("===================================================")
    print("           CodeAlpha JPG File Organizer            ")
    print("===================================================")

    # Use project-local paths
    source_dir = Path("source")
    dest_dir = Path("destination")
    
    print(f"Source folder: {source_dir}")
    print(f"Destination folder: {dest_dir}\n")

    # Check if source directory exists
    if not source_dir.exists() or not source_dir.is_dir():
        print(f"Error: The source directory '{source_dir}' does not exist.")
        print("Please create it and add some .jpg files before running this script.")
        return
        
    print("Scanning for JPG files...\n")
    
    # Ensure destination directory exists
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Error: Failed to create destination directory '{dest_dir}'.")
        print(f"Details: {e}")
        return

    files_found = 0
    files_moved = 0
    files_skipped = 0
    
    # Iterate through files in the source directory
    try:
        for file_path in source_dir.iterdir():
            # Check if it is a file and ends with .jpg or .JPG (case-insensitive check)
            if file_path.is_file() and file_path.suffix.lower() == ".jpg":
                files_found += 1
                
                dest_file_path = dest_dir / file_path.name
                
                # Check for duplicate in destination to avoid silent overwrite
                if dest_file_path.exists():
                    print(f"Skipped: {file_path.name} (File already exists in destination)")
                    files_skipped += 1
                    continue
                
                # Attempt to move the file
                try:
                    shutil.move(str(file_path), str(dest_file_path))
                    print(f"Moved: {file_path.name}")
                    files_moved += 1
                except PermissionError:
                    print(f"Error: Permission denied when moving '{file_path.name}'.")
                    files_skipped += 1
                except Exception as e:
                    print(f"Error: Failed to move '{file_path.name}'. Details: {e}")
                    files_skipped += 1
    except PermissionError:
        print("Error: Permission denied when accessing the source directory.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while scanning the source directory: {e}")
        return
        
    print("\n---------------------------------------------------")
    print(f"Files found  : {files_found}")
    print(f"Files moved  : {files_moved}")
    print(f"Files skipped: {files_skipped}")
    print("---------------------------------------------------\n")
    
    if files_found == 0:
        print("No JPG files were found in the source directory.")
    elif files_moved == files_found:
        print("Task completed successfully.")
    else:
        print("Task completed with some skipped files or errors.")

if __name__ == "__main__":
    main()
