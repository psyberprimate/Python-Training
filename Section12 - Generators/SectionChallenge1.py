import os
import fnmatch

def find_full_path(root, extension):
    for path, directories, files in os.walk(root):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            yield os.path.join(path, file)

for f in find_full_path('Section12 - Generators', 'emp3'):
    print(f)