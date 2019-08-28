import json
import os
import sqlite3
conn = sqlite3.connect('pin4ever.sqlite.db')
c = conn.cursor()

for row in c.execute("select name from boards"):
    folder = list(row)[0]
    print(folder)
    os.mkdir(folder)

for row in c.execute("select a.name, replace(b.img_src, rtrim(b.img_src, replace(b.img_src, '/', '')), '') from boards a, pins b where a.Board_ID = b.Board_ID"):
    filename = "D:\\tmp\\Pinterest\\"+list(row)[1]
    newFolder = "D:\\tmp\\Pinterest\\"+list(row)[0]+"\\"+list(row)[1]
    print filename, newFolder
    try:
        os.rename(filename, newFolder)
    except:
        continue
    
conn.close()
