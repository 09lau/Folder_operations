# srcfile 需要复制、移动的文件
# dstpath 目的地址

"""

glob.glob(path)的功能：
返回符合path格式的所有文件的路径，以list存储返回。
glob.iglob(path)的功能：
返回符合path格式的一个文件的路径。

path的表示方法：
利用匹配符："* "， “?”， “[ ]“来表示。其中，”*“表示匹配任意字符串，”?” 匹配任意单个字符， “[ ]” 匹配指定范围内的字符。

src：源文件夹或文件
dst：移动至dst文件夹，或将文件改名为dst文件。如果src为文件夹，而dst为文件将会报错
"""

import os
import shutil
from glob import glob

def moveFile(srcfile):  # 移动函数
    if  os.path.isfile(srcfile):
        print("%s 不是文件夹!" % (srcfile))
    else:
        dir_list = os.listdir(srcfile)  # 直接返回指定路径下，文件和文件名组成的列表
        # 文件夹分类
        # 1.移动文件地址自动生成
        dir_new_list = []
        classify_dis={}
        for i in dir_list:
            dir_new_list.extend(i[-4:-5:-1])

        dir_new_list=list(set(dir_new_list))
        # ❥(^_-)添加查询字典集
        for index in dir_new_list:
            classify_dis[index] = []
        print(classify_dis)

        # 2.判断分类文件是否存在
        for dst in dir_new_list:
            dir_new = os.path.join(src_dir, dst)
            if  not os.path.exists(dir_new):  # 文件不存在
                os.makedirs(dir_new)  # 创建路径
                print("%s 目标文件已生成"%(dir_new))
            else:
                print("%s 目标文件已存在"% (dir_new))
        # 目录文件分类
        # 1.直接返回指定路径下，文件和文件名组成的列表
        src_list = os.listdir(src_dir)
        print("dirlist is{}".format(src_list))  # 输出文件列表
        # 2.找到指定名称文件
        for k,v in classify_dis.items():
            Folder_name =k
            for name in src_list:
                if  Folder_name in name:
                    src_path=os.path.join(src_dir, name)
                    dst_dir=os.path.join(src_dir, Folder_name)
                    classify_dis[k]=dst_dir
                    # 移动文件
                    shutil.move(src_path,dst_dir)
                    print("从  %s  移到->  %s文件   " % (src_path,dst_dir))

"""
功能：大批量移动指定文件
1.根据所有文件名的规律自动生成一个子文件夹存放文件
2.根据文件夹名称查找所有文件的集合
3.移动文件夹
"""
src_dir = 'D:\MEDIA'
dst_dir = ''
# os.path.join()函数：连接两个或更多的路径名组件
# glob.glob(os.path.join(file_path, '*', '*.txt'))
src_file_list =glob(src_dir + '*') # glob获得路径下所有文件，可根据需要修改
for srcfile in src_file_list:
    moveFile(srcfile)  # 移动文件