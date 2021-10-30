# Turn the absolute paths to relative paths in a .m3u playlist

import sys
import os.path as path

# Check if a file was given
if len(sys.argv) < 2:
    print("Usage: python rel2abs.py [FILE]")
    exit(1)

# Open the file
f = open(sys.argv[1], 'r')

lines = f.readlines()
f.close()
f = open(sys.argv[1], 'w')

# str of new file
buffer = ""

# Replace the absolute path lines with their relative path
for line in lines:
    if line[0] != '#':
        line = path.relpath(line)
    buffer += line 

# Write the buffer to the file
f.write(buffer)
f.close()