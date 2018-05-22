#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
import subprocess

# ------------------ variables --------------
# 移动硬盘盘符列表
descriptors = [d + os.altsep for d in ('G:',)]
# 保留文件夹列表, 即：读取除此之外的所有文件夹
CONSERVATIVE_DIR = (str.upper('System Volume Information'), '$RECYCLE.BIN',)
# 目标文件夹列表，即：读取规定列表的文件夹
TARGET_DIR = ('20180518',)
# hdfs 存取路径
HADOOP_TARGET_PATH = '/Data'
HADOOP_CMD_PROFIX = 'D:/Hadoop/hadoop-3.0.2/bin/hadoop fs '

# -----------------  hdfs functions ----------------
def put(local_path, hadoop_path, overwrite):
    if not overwrite:
        cmd = HADOOP_CMD_PROFIX + "-put " + local_path + ' ' + hadoop_path
    else:
        cmd = HADOOP_CMD_PROFIX + "-put -f " + local_path + ' ' + hadoop_path
    print('COMMAND: ', cmd)
    os.system(cmd)

def mkdir(hadoop_path):
    cmd = HADOOP_CMD_PROFIX + "-mkdir " + hadoop_path
    print('COMMAND: ', cmd)
    os.system(cmd)

def lsr(hadoop_path):
    cmd = HADOOP_CMD_PROFIX + '-ls -R ' + hadoop_path
    print('COMMAND: ', cmd)
    os.system(cmd)

def test(hadoop_path):
    cmd = HADOOP_CMD_PROFIX + '-test -e ' + hadoop_path
    r = os.system(cmd)
    print('COMMAND: ', cmd, ' --> ', r)
    return r

def upload(overwrite, depth):

    # 检查用户
    user = os.environ['USERNAME']
    print('current user: ', user)
    if user!='hadoop':
        print('wrong user, now exit')
        sys.exit(1)

    for descriptor in descriptors:
        dirlist = os.listdir(descriptor)
        # 顶级过滤和筛选
        if CONSERVATIVE_DIR:
            dirlist = [dir for dir in dirlist if str.upper(dir) not in CONSERVATIVE_DIR]
        if TARGET_DIR:
            dirlist = [dir for dir in dirlist if dir in TARGET_DIR]

        # 创建 /Data 根目录
        if test(HADOOP_TARGET_PATH) == 1:
            mkdir(HADOOP_TARGET_PATH)

        # 需要特殊处理的文件夹
        SPECIAL = ('track',)

        if overwrite:                                 # 开启全覆盖，覆盖所有文件夹
            for dir in dirlist:
                local_path = descriptor+os.sep+dir
                hadoop_path = HADOOP_TARGET_PATH
                put(local_path, hadoop_path, overwrite)
        else:                                        # 关闭全覆盖
            for dir in dirlist:
                dir_tree = os.walk(descriptor+dir)
                for dirpath, dirnames, filenames in dir_tree:
                    nodes = dirpath.split(descriptor)[1].split(os.sep)

                    if len(nodes) > depth and nodes[depth-1] not in SPECIAL:
                        continue
                    elif len(nodes) > depth + 1 and nodes[depth-1] in SPECIAL:
                        continue

                    hadoop_path = HADOOP_TARGET_PATH + os.altsep + os.altsep.join(nodes)
                    if test(hadoop_path) == 1:
                        put(dirpath, hadoop_path, overwrite)

        lsr(HADOOP_TARGET_PATH)

# -------------------- call ------------------
overwrite = input('Mode Overwrite? (Y/N)')
depth = 3
if str.upper(overwrite) == 'Y':
    upload(True, depth)
elif str.upper(overwrite) == 'N':
    upload(False, depth)
else:
    sys.exit(1)

