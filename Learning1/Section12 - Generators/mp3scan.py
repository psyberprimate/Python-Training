import os
import fnmatch
import id3reader_p3 as id3reader


def find_music(start, extension):
    for path, directories, files in os.walk(start):
        for file in fnmatch.filter(files, '*.{}'.format(extension)):
            absolute_path = os.path.abspath(path)       # create absolute path
            yield os.path.join(absolute_path, file)              # use it in yielded values


my_music_files = find_music('Section12 - Generators/music', 'emp3')
# my_music_files = find_music('/Users/timbuchalka/Desktop/TestMusic/', 'mp3')

error_list = []
for f in my_music_files:
    try:
        id3r = id3reader.Reader(f)
        print("Artist: {}, Album: {}, Track: {}, Song: {}".format(
            id3r.get_value('performer'),
            id3r.get_value('album'),
            id3r.get_value('track'),
            id3r.get_value('title')
        ))
    except:
        error_list.append(f)


for error_file in error_list:
    print(error_file)
