import pandas as pd
import re
import pymysql
from queue import Queue
from treelib import Tree, Node
import json
from pyecharts import options as opts
from pyecharts.charts import  Tree as PyTree
global dict;
global id;
import sys
import os
import numpy as np
#数据库
DBHOST = 'localhost'
DBUSER = 'root'
DBPASS = '123456'
DBNAME= 'finger'
#
dict={} #全局dict
dict_key={} #统计key的频率
common_header = ['server','content-length','connection','pragma','transfer-enconding','upgrade','via','age','etag','location'
                 ,'vary','www-authenticate']  ##定义常用header
additional_figure= ['title','body'] ##附加特征

# common_header = ['server','content-length']  ##定义常用header
data=[]
sqldata = []
finger_countlist = np.array([])
##函数作用 读取dir_file文件，产生字典


def read_tocsv(dir_file):
    df = pd.read_json(dir_file, lines=True)  ## 读取json数据
    df['first_time'] = df['first_time'].dt.tz_localize(None)  ##删除时区数据
    df['day_time'] = df['day_time'].dt.tz_localize(None)  ##删除时区数据
    df = df['data'].apply(pd.Series)  ## 拆分data数据
    header = df['header']
    # header.to_csv('header.csv')
    header_list = header.tolist()
    for i in header_list: ##i为每一个header 对象
        temp_dict={}## 临时变量 用于生成一个字典对象
        str = re.sub('(\r\n)+', '\r\n', i)
        i = str.split('\r\n')
        for j in i:##j为header中的每一行对象
            try:
                if j == '' or '\n' in j or '<' in j:  ##筛选出符合规则的key
                    continue
                else:
                    j = j.split(':', 1)
                    key = j[0].lower()
                    key = key.replace(" ","")
                    value = j[1]
                    temp_dict[key]=value
                    if key in dict:
                        dict[key].append(value)
                        dict_key[key]+=1
                    else:
                        dict.setdefault(key, [])
                        dict[key].append(value)
                        dict_key.setdefault(key,0)
            except:
                continue
        data.append(temp_dict)

    # 根据字典的每一个值创建一个pd.df对象






def select_primaryheader(datalist): ##加一个功能 添加server信息
    for i in datalist:
        for key in list(i.keys()):
            if key not in common_header and key not in additional_figure :
                del i[key]
            if key != 'server':
                i[key] += "@"
                i[key] += i['server']
    return datalist


def normalizationdata(datalist):  ##对数据进行归一化处理 没有的字段置为null
    for i in datalist:
        for key in common_header:
            if key not in list(i.keys()):
                i[key]='null'
        for key in list(i.keys()):
            i[key]=str(i[key]).replace(" ", "")
            key=key.replace(" ", "")
            if key not in common_header and key not in additional_figure:
                del i[key]
    return datalist

def clean_server(datalist):##去除server的多余版本号
    for i in datalist:
        i["server"]=i["server"].split("/", 1)[0]
    return datalist

def sort(datalist,key): ##将指定的list 依据 所给key 进行筛选排序 返回的是一个嵌套的列表 和带有词频信息的列表
    key_index={} ##用来存不同key值所对应的list的下标
    Frequency={}
    redata=[]
    tempindex=0
    for i in datalist:
        try:
            if (i[key] not in key_index.keys()):
                key_index[i[key]] = tempindex
                Frequency[i[key]] = 1
                redata.append([])
                redata[key_index[i[key]]].append(i)
                tempindex = tempindex + 1
            else:
                Frequency[i[key]] += 1
                redata[key_index[i[key]]].append(i)
        except:
            continue
    Frequency = sorted(Frequency.items(), key=lambda x: x[1], reverse=True) ##词频信息从大到小
    tempFe=[]
    for i in Frequency:
        tempFe.append(i)
    Frequency = tempFe
    return redata,Frequency





def read_data(path):
    file_name = os.listdir(path)
    count=0
    for i in file_name:
        print("count:",count)
        file_path = '' + path + '\\' + i
        read_tocsv(file_path)
        count+=1
        if count==1:
            break
    return data

# path='./dataset'
# file_name = os.listdir(path)
# for i in file_name:
#     file_path=''+path+'\\'+i
#     read_tocsv(file_path)





#################################
# keys = pd.DataFrame(list(dict.keys()),columns=['keys'])
## keys.to_csv('keys_0.csv')
# read_tocsv('./dataset/http_101_AType_CN_20221011103634533_0.json')
#################################




def data_processing(_data):
    data = normalizationdata(_data)
    data = clean_server(data)
    data = select_primaryheader(data)
    return data



def create_fingerTree(data):
    global finger_countlist
    id = 0
    rootqueue = Queue()
    tree = Tree()
    tree.create_node("root", 0)
    list, fre = sort(data, "server")
    for i in fre:
        id += 1
        rootqueue.put(id)
        tree.create_node(i[0], id, 0)

    for key in common_header:
        if (key == 'server'):  ##已经分了server
            continue
        TempList = []
        for l in list:
            parents = rootqueue.get()
            temp, children = sort(l, key)
            for j in temp:
                TempList.append(j)
            for i in children:
                id += 1
                rootqueue.put(id)
                nodename = ""
                nodename += key
                nodename += ":"
                nodename += i[0].split('@')[0]
                if key == common_header[-1]:
                    nodename += "#"
                    nodename += str(i[1])
                    finger_countlist = np.append(finger_countlist, i[1])
                try:
                    tree.create_node(nodename, id, parents)
                except:
                    continue
                    print("error")
        list = TempList
    return tree
######





#################################
# f=open('tree.txt','w')
# sys.stdout=f
# print(tree.show())
#################################


# tree.show(key=False)
#
# jsondata=tree.to_json(sort=False)
# redata = json.loads(jsondata)
# with open('./treedata.json','w') as f:
#     json.dump(redata,f)


def cut_leaf(Tree):
    path_len = len(Tree.paths_to_leaves())
    for j in range(path_len):
        if j==path_len:
            break
        print(j,path_len)
        path = Tree.paths_to_leaves()[j]
        print(path)
        for i in path:
            nid = Tree.get_node(i)
            if (nid.tag.split(':')[-1] == "null"):
                Tree.link_past_node(i)
        path_len = len(Tree.paths_to_leaves())
    return Tree


def transform_json(data):
    key, value = list(data.items())[0]
    lst = []
    for child in value['children']:
        if isinstance(child, dict):
            lst.append(transform_json(child))
        else:
            lst.append({'name': child})
    return {'name': key, "children": lst}

def get_html(tree):
    str = tree.to_json(sort=False)
    jsondata = json.loads(str)
    transformdata = transform_json(jsondata)
    tree = (
        PyTree(init_opts=opts.InitOpts(width="1800px", height="800px"))
        .add("", [transformdata], orient="LR", initial_tree_depth=1, collapse_interval=-1, is_roam=True)
        #     参数layout的"radial"是径向布局是指以根节点为圆心，每一层节点为环，而"orthogonal"是正常的水平和垂直布局
        #     参数symbol是标记类型形状，提供的类型有:'emptyCircle', 'circle', 'rect', 'roundRect','triangle', 'diamond', 'pin', 'arrow'
        #     参数orient是布局方向，水平从左到右为"LR"，水平从右往左为"RL"，垂直从上到下为"TB",垂直从下到上为"BT"
        .set_global_opts(title_opts=opts.TitleOpts(title="指纹树"),
                         legend_opts=opts.LegendOpts(type_="scroll", pos_left="left", orient="vertical", )
                         )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    tree.render("./devicetree.html")


def cal_percentile(Countlist):
    mid =np.median(Countlist)
    quarter = np.percentile(Countlist,25)
    quarter3 = np.percentile(Countlist,75)
    most = np.percentile(Countlist,98)
    return mid,quarter,quarter3,most


# def to_txt(path):
#     f = open(path, 'w')
#     sys.stdout = f
#     print(tree.show())


#################################



#



#################################
# begin=0
# for j in dict["server"]:
#     dict["server"][begin]=j.split("/", 1)[0]
#     begin=begin+1
# for i in dict.keys():  ##key中的值存在大小写的不同
#     try:
#         df = pd.DataFrame(dict[i], columns=[i])
#         # df.to_csv('./header/' + i + '.csv')
#     except:
#         continue
#
# df=pd.DataFrame(dict_key,index=[0])
# df.to_csv('./key_count.csv')
# print(dict["server"])
#################################

def sql_processed(dir_file):
    df = pd.read_json(dir_file, lines=True)  ## 读取json数据
    df['first_time'] = df['first_time'].dt.tz_localize(None)  ##删除时区数据
    df['day_time'] = df['day_time'].dt.tz_localize(None)  ##删除时区数据
    df = df['data'].apply(pd.Series)  ## 拆分data数据
    ##加特征
    for index, row in df.iterrows():
        header = row['header']
        body = row['body']
        title = row['title']
        ##处理header并分词
        temp_dict={}## 临时变量 用于生成一个字典对象
        string = re.sub('(\r\n)+', '\r\n', header)
        header = string.split('\r\n')
        for j in header:##j为header中的每一行对象
            try:
                if j == '' or '\n' in j or '<' in j:  ##筛选出符合规则的key
                    continue
                else:
                    j = j.split(':', 1)
                    key = j[0].lower()
                    key = key.replace(" ","")
                    value = j[1]
                    temp_dict[key]=value
                    if key in dict:
                        dict[key].append(value)
                        dict_key[key]+=1
                    else:
                        dict.setdefault(key, [])
                        dict[key].append(value)
                        dict_key.setdefault(key,0)
            except:
                continue
        temp_dict['title']=title
        temp_dict['body'] = body
        sqldata.append(temp_dict)

def write2sql(data):
    db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
    num = len (data)
    count=0
    cur = db.cursor()

    sqlQuery = "CREATE TABLE Finger(Server VARCHAR(1000) NOT NULL ,content_length CHAR(255),connection_ CHAR(255),pragma TEXT,transfer_enconding TEXT,upgrade CHAR(255),via TEXT," \
               "age CHAR(255),etag TEXT,location TEXT,vary CHAR(255),www_authenticate TEXT,title TEXT,body MEDIUMTEXT)"
    cur.execute(sqlQuery)
    for finger in data:
        print(count,num)
        count+=1
        strlist = []
        for key in common_header:
            strlist.append(finger[key].split('@')[0])
        for add_key in additional_figure:
            strlist.append(finger[add_key].split('@')[0])
        try:
            db.ping()
        except:
            db = pymysql.connect(host=DBHOST, user=DBUSER, password=DBPASS, database=DBNAME)
            cur = db.cursor()
        sqlQuery = " INSERT INTO Finger (Server,content_length,connection_,pragma,transfer_enconding,upgrade,via,age,etag,location,vary,www_authenticate,title,body) " \
                   "VALUE (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        value = []
        for i in range(len(common_header)+len(additional_figure)):
            value.append(str(strlist[i]))
        value = tuple(value)
        cur.execute(sqlQuery, value)
        db.commit()
    db.close()

def read_sql_Data(path):
    file_name = os.listdir(path)
    print(file_name)
    count=1
    for i in file_name[0:10]:
        print("count:",count)
        # count+=1;
        file_path = '' + path + '\\' + i
        sql_processed(file_path)
        count+=1
    return sqldata



if __name__ == '__main__':

    path = './dataset'
    sql_data = read_sql_Data(path)
    sql_data = data_processing(sql_data)
    write2sql(sql_data)

    # path = './dataset'
    # data = read_data(path)
    # processed_data = data_processing(data)
    # tree = create_fingerTree(processed_data)
    # mid,quarter,quarter3,most = cal_percentile(finger_countlist)
    # print(mid,quarter,quarter3,most)
    # print(finger_countlist)
    # print(np.sum(finger_countlist))
    # # tree = cut_leaf(tree)
    # tree.save2file('./tree.txt', key=False)



    # jsondata = tree.to_json(sort=False)
    # redata = json.loads(jsondata)
    # with open('./treedata.json', 'w') as f:
    #     json.dump(redata, f)

