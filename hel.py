# import pandas as pd
import json
# with open('http_101_AType_CN_20221011103634533_0.json',encoding="utf-8") as f:
#     superHeroSquad = json.load(f)
# print(type(superHeroSquad))  # Output: dict
#
# print(superHeroSquad.keys())
import pandas as pd
import xlsxwriter
df = pd.read_json('./dataset/http_101_AType_CN_20221011103634533_0.json', lines=True) ##



df['first_time']=df['first_time'].dt.tz_localize(None) ##删除时区数据
df['day_time']=df['day_time'].dt.tz_localize(None)  ##删除时区数据

df.to_excel("info.xlsx") ##



data=df['data']
data=data.apply(pd.Series)
data.to_excel("data.xlsx")

clean_data=df['data'].apply(pd.Series) ## 拆分data数据

# clean_cve = df['cve_detail'].apply(pd.Series) ## 拆分cve 嵌套
# clean_refer = df['refer_os'].apply(pd.Series) ## 拆分refer_os 嵌套
# clean_ref_os = df['ref_os'].apply(pd.Series) ##拆分ref_os嵌套

# clean_data.to_excel('clean_data.xlsx', engine='xlsxwriter', index=False, encoding='utf-8') ##删除xlsx中的错误编符号
# clean_cve.to_excel('clean_cve.xlsx', engine='xlsxwriter', index=False, encoding='utf-8') ##cve列数据难搞
# clean_refer.to_excel('clean_refer.xlsx', engine='xlsxwriter', index=False, encoding='utf-8') ##列表嵌套字典
# clean_ref_os.to_excel('clean_ref.xlsx', engine='xlsxwriter', index=False, encoding='utf-8') ##列表嵌套字典

#
# clean_data=pd.concat([clean_data['web'].apply(pd.Series),clean_data['xmap'].apply(pd.Series),
#                      clean_data.drop('web',axis=1),clean_data.drop('xmap',axis=1)],axis=1)


clean_data = pd.concat([clean_data['web'].apply(pd.Series),clean_data['xmap'].apply(pd.Series),
                        clean_data.drop(["web","xmap"],axis=1)],axis=1)

df =pd.concat([clean_data,df.drop('data',axis=1)],axis=1)

df.to_excel('clean_data.xlsx', engine='xlsxwriter', index=False, encoding='utf-8') ##删除xlsx中的错误编符号
print(clean_data['ref_product'])
print(clean_data.columns.values)
index=clean_data.columns.values

j=0

for i in df.columns.values:
    try:
        df[i].value_counts().reset_index(name='count').to_csv('./频率/'+i+'.csv')
    except:
        pass
    continue



# clean_web = clean_data['web'].apply(pd.Series)  ##拆分data数据中的web列

# df = pd.concat([df['data'].apply(pd.Series), df.drop('data', axis = 1)], axis = 1) ##将data嵌套拆开
# df.to_excel('info.xlsx', engine='xlsxwriter', index=False, encoding='utf-8') ##删除xlsx中的错误编符号





# df.to_excel("info1.xlsx")
# print(df.dtypes)

# with open('http_101_AType_CN_20221011103634533_0.json',encoding='utf-8') as f:
#     df = json.load(f)
# out = pd.json_normalize(df, record_path=['data'])
