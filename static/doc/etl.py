# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:20:49 2024

@author: 11107045
"""
import psycopg2
import json 
#PostgreSQL
import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('FHIR第三版.xlsx')

# 打印 DataFrame 的内容
table=[]
column=[]
#print(df[' 資料庫.欄位名稱'])
for di in range(len(df[' 資料庫.欄位名稱'])):
    table.append(df[' 資料庫.欄位名稱'][di].split('.')[0])
    column.append(df[' 資料庫.欄位名稱'][di].split('.')[1])
print(table,column)

ip='10.221.252.50'
port='5432'
database='BASE'
username='wiadvance'
password='TEpVSENLaFBkCg'

jsonPath='Resource.json'
cancerflattenjson = json.load(open(jsonPath,encoding="utf-8"))
list_of_key = list(cancerflattenjson.keys())
list_of_value = list(cancerflattenjson.values())
jsonPath='Roche_example0322.json'
cancerbasejson = json.load(open(jsonPath,encoding="utf-8"))

#conn = psycopg2.connect(database='', user='ID', password='PassWord', host='IP', port='Port')
#cur = conn.cursor()
#consentsql = "SELECT column_name,data_type FROM information_schema.columns WHERE table_name = 'reportxml';"
#cur.execute(consentsql)
#rows = cur.fetchall()

#print(len(rows))
for i in range(len(list_of_value)):
    if 'SQL' in str(list_of_value[i]):
        keylist=str(list_of_key[i]).split('_')
        #print(str(list_of_value[i]).split('_'))
        
        #sqlstr='select ' + list_of_value[i].split('_')[2] + ' from ' + list_of_value[i].split('_')[1]
        #cur.execute(sqlstr)
        #rows = cur.fetchall()
        for key in keylist:
            cancerbasejson['identifier']['use']
