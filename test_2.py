# -*-coding:utf-8 -*-

def str_update(config):
    file_open = open(config["file_read"],"r",encoding='utf-8')
    file_write = open(config["file_write"],"a+")
    lists = file_open.readlines()
    #print(lists)
    for list in lists:
        #print(list)
        list_new = list.replace(' ','\t').replace('_','-')
        #print(list_new)
        file_write.write(list_new)
    file_open.close()
    file_write.close()
if __name__ == "__main__":
    config = {
        "file_read":"D:/Python27/python_test/test_2.txt",
        "file_write":"D:/Python27/python_test/test_2_update.txt",
    }
    str_update(config)