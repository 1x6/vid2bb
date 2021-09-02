import os, re

ext = input('Enter the files\' extension: (e.g .mkv) ')

directory = os.getcwd()
for filename in os.listdir(directory):
    if filename.endswith(ext):
        print(filename)
        new_fn = re.sub(ext,  '.3gp', filename)
        os.popen(f'''ffmpeg -y -i "{filename}" -r 20 -s 352x288 -vb 400k -acodec aac -strict experimental -ac 2 -ab 128k "{new_fn}"''')
    else:
        continue
