"""
This script recursively searches files in the specified folder
and changes their modification time to be the same as their creation time.
Usage:
python change_mtime_to_be_same_as_ctime_recursively.py <folder_path>
"""

import os
import sys

def change_mtime_to_be_same_as_ctime_recursively(folder_path):
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Get the creation and modification times
                creation_time = os.path.getctime(file_path)
                modification_time = os.path.getmtime(file_path)

                # If modification time is different from creation time, update it
                if modification_time != creation_time:
                    os.utime(file_path, (creation_time, creation_time))
                    print(f"Updated: {file_path}")
                else:
                    print(f"Skipped (already matching): {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python change_mtime_to_be_same_as_ctime_recursively.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print(f"Error: {folder_path} is not a valid directory.")
        sys.exit(1)

    change_mtime_to_be_same_as_ctime_recursively(folder_path)