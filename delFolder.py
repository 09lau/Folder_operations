#!python3

"""
❥(^_-)❥(^_-)❥(^_-)❥(^_-)
功能
保留含有name的文件，
删除path的内容下的文件
"""
import turtle
import os
"""设置主文件夹路径"""
path = 'D:\EFI'
Folder_name='F'
if not os.path.exists(path):  # 判断路径是否正确，如果没有就创建这个文件夹
    os.makedirs(path)
if os.path.isdir(path): #判断是否是文件夹
    dir_list = os.listdir(path)   #直接返回指定路径下，文件和文件名组成的列表
print("path={}".format(path))  # 输出地址
print("dirlist is{}".format(dir_list)) #输出文件列表

for i, dir_name in enumerate(dir_list): # enumerate（）对一个列表，既要遍历索引又要遍历元素  接收第二个参数，用于指定索引起始值
    """找到并删除文件"""
    file = os.listdir(path)  # 返回当前目录文件
    for i, name in enumerate(file):
        if not Folder_name in name:
            path_delete = os.path.join(path, name)
            os.remove(path_delete)
            print('{} 已删除\n'.format(path_delete))
print("FINISHED!")
