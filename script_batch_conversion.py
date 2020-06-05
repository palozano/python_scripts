import os
import subprocess

path = ''
files = list()

# change spaces for underscores, and to lowercase
for f in os.listdir(path):
    os.rename(os.path.join(path, f), os.path.join(path, f).replace(' ', '_').lower())

# walk the path finding epub files
for r, d, f in os.walk(path):
    for file in f:
        if '.epub' in file:
            files.append(os.path.join(r, file))

# use .kindlegen script (i suppose it's in the same folder)
# to convert .epub to .mobi in the terminal
for f in files:
    process = subprocess.run('./kindlegen {}'.format(f), shell=True)
