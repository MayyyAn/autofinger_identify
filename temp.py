# # 数据路径
# import json
#
# path = "./dataset/http_101_AType_CN_20221011103634533_0.json"
# # 读取文件数据
#
# # 由于文件中有多行，直接读取会出现错误，因此一行一行读取
# file = open("./dataset/http_101_AType_CN_20221011103634533_0.json", 'r', encoding='utf-8')
# papers = []
# for line in file.readlines():
#     dic = json.loads(line)
#     print(dic)
#     papers.append(dic)
#
# print(len(papers))




# 用于测试小规模数据

from __future__ import print_function
import json
import sys
import numpy as np
from pyecharts.charts import  Tree as PyTree
from treelib import Node, Tree
from pyecharts import options as opts
from treelib import Tree, Node
from pyecharts.render import make_snapshot
from snapshot_phantomjs import snapshot
import json
from queue import Queue
import  graphviz


common_header = ['server','connection','content-type','location','content-length']



data=[
{"server":"nginx","content-type":"text/html","content-length":"1","connection":"1"},
{"server":"nginx","content-type":"text/html","content-length":"1"},
{"server":"nginx","content-type":"text/html","content-length":"1"},
{"server":"nginx","content-type":"text/html","content-length":"1"},
{"server":"nginx","content-type":"text/html","content-length":"2"},
{"server":"nginx","content-type":"text/html","content-length":"33"},
{"server":"nginx","content-type":"text/html","content-length":"12"},
{"server":"nginx","content-type":"text/html","content-length":"15"},
{"server":"nginx","content-type":"text/html","content-length":"16"},
{"server":"apache","content-type":"json","content-length":"149","connection":"1"},
{"server":"apache","content-type":"json","content-length":"13"},
{"server":"apache","content-type":"json","content-length":"149"},
{"server":"zit","content-type":"json","content-length":"149"},

#注意key -value中的 value可能会出现格式的错误 后续操作需要加上对空格的处理

]


def select_primaryheader(datalist):
    for i in datalist:
        for key in list(i.keys()):
            if key not in common_header:
                del i[key]
    return datalist


def sort(datalist,key): ##将指定的list 依据 所给key 进行筛选排序 返回的是一个嵌套的列表 和带有词频信息的列表
    key_index={} ##用来存不同key值所对应的list的下标
    Frequency={}
    redata=[]
    tempindex=0
    for i in datalist:
        if (i[key] not in key_index.keys()):
            key_index[i[key]]=tempindex
            Frequency[i[key]]=1
            redata.append([])
            redata[key_index[i[key]]].append(i)
            tempindex=tempindex+1
        else:
            Frequency[i[key]]+=1
            redata[key_index[i[key]]].append(i)
    Frequency = sorted(Frequency.items(), key=lambda x: x[1], reverse=True) ##词频信息从大到小
    tempFe=[]
    for i in Frequency:
        tempFe.append(i)
    Frequency = tempFe
    return redata,Frequency


def normalizationdata(datalist):  ##对数据进行归一化处理 没有的字段置为null
    for i in datalist:
        for key in common_header:
            if key not in list(i.keys()):
                i[key]='null'
        for key in list(i.keys()):
            i[key]=i[key].replace(" ", "")
            key=key.replace(" ", "")
            if key not in common_header:
                del i[key]
    return datalist

def select_primaryheader(datalist): ##加一个功能 添加server信息
    for i in datalist:
        for key in list(i.keys()):
            if key not in common_header:
                del i[key]
            if key != 'server':
                i[key] += "@"
                i[key] += i['server']
    return datalist

# #返回的fre为 字符型列表


def tree2printing():
    path_list = []
    print_list = []
    for path in tree.paths_to_leaves():
        tag_list = []
        for nid in path:
            node = tree.get_node(nid)
            tag_list.append(node.tag)
        path_list.append(tag_list)
    for item in path_list:
        finger_num = item[-1]
        finger = ''
        item = [x for x in item if x.split(':')[-1]!='null']
        finger = "&&".join(item[1:-1])
        print_list.append((finger,finger_num))
    return print_list








# global tree
# tree=""

# def add_node(root,children):  ##r
#     global tree
#     tree+=root
#     tree+=":"
#     for i in range(len(children)):
#         if(i==len(children)-1):
#             tree+=children[i]
#         else:
#             tree+=children[i]
#             tree+=","
#     tree+=";"
#     return tree


data=normalizationdata(data)  ##数据升维
data=select_primaryheader(data) ##数据加主键


id=0

rootqueue=Queue()
tree=Tree()
tree.create_node("root",0)
#tree.create_node() paramater:tag,id,root

List,fre=sort(data,"server")


for i in fre:
    id+=1
    rootqueue.put(id)
    node=tree.create_node(i[0],id,0)

lastroot="root"


finger_countlist = np.array([])

for key in common_header:
    if(key=='server'): ##已经分了server
        continue
    TempList=[]
    for l in List:
        parents=rootqueue.get()
        temp,children=sort(l,key)
        for j in temp:
            TempList.append(j)
        for i in children:
            nodename=""
            nodename+=key
            nodename+=":"
            nodename+=i[0].split('@')[0]
            if key==common_header[-1]:
                nodename+="#"
                nodename+=str(i[1])
                finger_countlist =np.append(finger_countlist,i[1])
            id += 1
            rootqueue.put(id)
            try:
                tree.create_node(nodename, id, parents)
            except:
                continue
    List=TempList




count = 0
path_len = len(tree.paths_to_leaves())

##减枝操作
# for j in range(path_len):
#     # print(j,path_len)
#     path = tree.paths_to_leaves()[j]
#     for i in path:
#         nid = tree.get_node(i)
#         if (nid.tag.split(':')[-1] == "null"):
#             tree.link_past_node(i)
#     path_len = len(tree.paths_to_leaves())





###错误版的减枝操作
# for path in tree.paths_to_leaves():
#     print(path)
#     for j in path:
#         nid = tree.get_node(j)
#         print(nid)
#         try:
#             if (nid.tag.split(':')[-1] == "null"):
#                 tree.link_past_node(j)
#         except:
#             continue

tree.show(key=False)
# tree.save2file('./tree.txt',key=False)


#############################计算指纹分位数










############################输出资产书多的指纹
print_list = tree2printing()
print(print_list)
fp = open('./finger.txt','w')
for item in print_list:
    printing = item[0]
    Last_figure = item[1]
    numcount = int(Last_figure.split('#')[-1])
    printing+="&&"
    printing+=Last_figure.split('#')[0]
    if numcount>=1:
        out='数量{},{}'.format(numcount,printing)
        with open('finger.txt', 'a') as fp:
            fp.write(out+'\n')
    fp.close()
############################
# print(np.sum(finger_countlist))



############################输出所有指纹
print_list = tree2printing()
for item in print_list:
    printing = item[0]
    Last_figure = item[1]
    printing+="&&"
    printing+=Last_figure.split('#')[0]
    print(printing)
############################


jsondata=tree.to_json(sort=False)
redata = json.loads(jsondata)
with open('./treedatatemp.json','w') as f:
    json.dump(redata,f)

# import pymysql
# DBHOST = 'localhost'
# DBUSER = 'root'
# DBPASS = '123456'
# DBNAME= 'dbtest'




# common_header = ['server','content-type','content-length','location','connectino']
# db = pymysql.connect(host=DBHOST,user=DBUSER,password=DBPASS,database=DBNAME)
# cur = db.cursor()
# # sqlQuery = "CREATE TABLE Finger(Server CHAR(20) NOT NULL ,Content_type CHAR(20),content_length CHAR(20),connection CHAR(20),location CHAR(20))"
# # cur.execute(sqlQuery)
#
#
# for finger in data:
#     strlist = []
#     for figure in finger.values():
#         strlist.append(figure.split('@')[0])
#     sqlQuery = " INSERT INTO Finger (Server, Content_type, content_length,connection,location) VALUE (%s,%s,%s,%s,%s) "
#     value = []
#     for i in range(len(common_header)):
#         value.append(str(strlist[i]))
#     value = tuple(value)
#     cur.execute(sqlQuery,value)
#     db.commit()
# db.close()