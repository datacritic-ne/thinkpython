#! python3

import os, glob
from filecmp import cmp

from pathlib import Path

# search for duplicates in /home/nemptage
# 1. Recursively search the directory and all subdirectories, return a list of complete paths for all files with, e.g., .txt
# 2. Within that list, use md5sum to compute checksum for all files
# 3. Find files with the same checksum value, how to use linux command diff as a second check?

p = Path('/home/nemptage') # the directory we're walking

text_files = []

for folderName, subfolder, filename in os.walk(p):
    # use glob to search for files with a .txt (or another) extension
    for sub in subfolder:
        for file in filename:
            if file in glob.glob('*.txt'):
                text_files.append(os.path.abspath(file))

text_files = sorted(text_files)

duplicates = []

for file in text_files:

    is_duplicate = False

    for class_ in duplicates:
        is_duplicate = cmp(file, class_[0], shallow=False)

        if is_duplicate:
            class_.append(file)

    if not is_duplicate:
        duplicates.append([file])

if duplicates:
    print("Duplicate files found:")
    for file in duplicates:
        print(file)
else:
    print("No duplicate files found.")