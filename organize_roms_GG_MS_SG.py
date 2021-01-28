import os
import shutil
import functools
import zipfile
import re

from functools import partial

def makefolders(root_dir, subfolders):
    concat_path = partial(os.path.join, root_dir)
    makedirs = partial(os.makedirs, exist_ok=True)
    for path in map(concat_path, subfolders):
        makedirs(path)

if __name__ == '__main__':
    root_dir = 'Z:\\Sega - Game Gear'
    subfolders = ('USA', 'Europe','World')
    makefolders(root_dir, subfolders)

if __name__ == '__main__':
    root_dir = 'Z:\\Sega - Master System - Mark III'
    subfolders = ('USA', 'Europe','World')
    makefolders(root_dir, subfolders)

if __name__ == '__main__':
    root_dir = 'Z:\\Sega - Mega Drive - Genesis'
    subfolders = ('USA', 'Europe','World')
    makefolders(root_dir, subfolders)


for filename in os.listdir('Z:\\Sega - Game Gear'):
    if re.match('[.*USA.*]', filename):
        shutil.move(os.path.join('Z:\\Sega - Game Gear', filename), 'Z:\\Sega - Game Gear\\USA')
    elif re.match('[.*\(Europe\).*]', filename):
        shutil.move(os.path.join('Z:\\Sega - Game Gear', filename), 'Z:\\Sega - Game Gear\\Europe')
    elif re.match('[.*World.*]', filename):
        shutil.move(os.path.join('Z:\\Sega - Game Gear', filename), 'Z:\\Sega - Game Gear\\Wolrd')


for filename in os.listdir('Z:\\Sega - Master System - Mark III'):
    if re.match('[.*USA.*]', filename):
        shutil.move(os.path.join('Z:\\Sega - Master System - Mark III', filename), 'Z:\\Sega - Master System - Mark III\\USA')
    elif re.match('[.*\(Europe\).*]', filename):
        shutil.move(os.path.join('Z:\\Sega - Master System - Mark III', filename), 'Z:\\Sega - Master System - Mark III\\Europe')
    elif re.match('[.*World.*]', filename):
        shutil.move(os.path.join('Z:\\Sega - Master System - Mark III', filename), 'Z:\\Sega - Master System - Mark III\\Wolrd')

for filename in os.listdir('Z:\Sega - Mega Drive - Genesis'):
    if re.match('[.*USA.*]', filename):
        shutil.move(os.path.join('Z:\\Sega - Mega Drive - Genesis', filename), 'Z:\\Sega - Mega Drive - Genesis\\USA')
    elif re.match('[.*\(Europe\).*]', filename):
        shutil.move(os.path.join('Z:\\Sega - Mega Drive - Genesis', filename), 'Z:\\Sega - Mega Drive - Genesis\\Europe')
    elif re.match('[.*World.*]', filename):
        shutil.move(os.path.join('Z:\S\ega - Mega Drive - Genesis', filename), 'Z:\\Sega - Mega Drive - Genesis\\Wolrd')
