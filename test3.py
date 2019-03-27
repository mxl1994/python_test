# -*-coding:utf-8 -*-
def list_file():
    file_open = open(config["file_read"], "r", encoding="utf-8")
    file_write = open(config["file_write"], "a+")
    lists = file_open.readlines()
    print(lists)
    list_strs = []
    for ele in lists:
        list_str = ele.strip("\n").split("\t")
        for str in list_str:
            list_strs.append(str)
    print(list_strs)
    #开始统计字符串的次数
    dic = {}
    for strs in list_strs:
            dic[strs] = list_strs.count(strs)
    print(dic)
    for k,v in dic.items():
        print('{k}:{v}'.format(k = k,v = v))
        file_write.write('{k}:{v}'.format(k = k,v = v)+"\n")
if __name__ == "__main__":
    config = {
        "file_read": "D:\Python27\python_test/test_3.txt",
        "file_write": "D:/Python27/python_test/test_3_result.txt",
    }
    list_file()