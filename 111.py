# coding: utf-8
"""
遍历C盘下的所有dll文件
"""
import os
import fnmatch


def main():
    f = open('dll_list.txt', 'w')
    for root, dirs, files in os.walk('c:\\'):
        for name in files:
            if fnmatch.fnmatch(name, '*.dll'):
                f.write(os.path.join(root, name))
                f.write('\n')
    f.close()
    print 'done...'


if __name__ == '__main__':
    main()