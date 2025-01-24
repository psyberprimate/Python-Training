import os

root = "Section12 - Generators/music"#"Section12 - Generators/music.zip"#"Section12 - Generators/music"

for path, directories, files in os.walk(root, topdown=True):
    print(path)
    first_split = os.path.split(path)
    print(first_split)
    second_split = os.path.split(first_split[0])
    print(second_split)
    for f in files:
        songs_details = f[:-5].split(' - ')
        print(songs_details)
    print('*'*40)