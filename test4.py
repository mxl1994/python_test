#-*-coding:utf-8 -*-
import os
def getfile_path(path):
    dirs = os.listdir(path)
    for file in dirs:
        #print(file)
        file_dir = os.path.join(path, file)
        if os.path.isdir(file_dir):
            #print(file_diir)
            getfile_path(file_dir)
        else:
            file_name = os.path.splitext(file)[0]
            file_format = os.path.splitext(file)[1]
            file_path = os.path.dirname(file_dir)
            #print(file_path)
            if file_format == ".txt":
                file_write.write(file_name + ":" + file_path+"\n")
            else:
                continue

def list_file_work(path):
    for fpath,dirs,files in os.walk(path):
        print(fpath)
        print(dirs)
        print(files)
        for file in files:
            #file_name = os.path.splitext(file)[0]
            file_format = os.path.splitext(file)[1]
            if file_format == ".txt":
                file_write.write(file + ":" + fpath+ "\n")
            else:
                continue
    file_write.close()

if __name__ == "__main__":
    dir = 'c:/'
    file_write = open(r"D:/Python27/python_test/test4.txt","a")
    '''getfile_path(dir)
    file_write.close()'''
    list_file_work(dir)