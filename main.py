import os, re

ext = input('Enter the files\' extension: (e.g .mkv) ')
directory = input('Enter the directory to look through: ')

for filename in os.listdir(directory):
    if filename.endswith(ext):
        print(filename)
        new_fn = re.sub(ext,  '.3gp', filename)
        os.popen(f'''ffmpeg -y -i "{directory}/{filename}" -r 20 -s 352x288 -vb 400k -acodec aac -strict experimental -ac 2 -ab 128k "{directory}/{new_fn}"''')
    else:
        continue
