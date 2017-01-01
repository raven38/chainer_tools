import os
import shutil

baseDir = './img/'
files = os.listdir(baseDir)

for file in files:
    date = file[:8]
    save_dir = './img/img/' + date

    try:
        os.mkdir(save_dir)
        cnt = 1
    except OSError as e:
        pass

    shutil.copy(baseDir + file, save_dir + '/image_%07d' %cnt + ".jpg")

    cnt += 1
