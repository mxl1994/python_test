# -*-coding:utf-8 -*-
def list_uniq():
    list = ['h','d','a','g','r','e','i','h','j','k','f','d','h','g','k','j','a']
    list_new = []
    for i in list:
        if i in list_new:
            continue
        else:
            list_new.append(i)
    print(list_new)
if __name__ =="__main__":
    list_uniq()