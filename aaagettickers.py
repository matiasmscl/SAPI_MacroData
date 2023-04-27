#!/usr/bin/env python
# coding: utf-8

import pandas
import os

if os.path.exists('info.csv'):
    Matriz_info=pandas.read_csv('info.csv')
    Matriz_info=Matriz_info.set_index('ticker')
else:
    Matriz_info=pandas.DataFrame()

Paginas=pandas.read_json('https://www.econdb.com/api/series/?page=1&format=json').loc[0,'pages']

Paginas=pandas.read_json('https://www.econdb.com/api/series/?page=1&format=json').loc[0,'pages']
for page in range(1,Paginas+1):
    try:
        df = pandas.read_json('https://www.econdb.com/api/series/?page='+str(page)+'&format=json')
        for line in range(len(df)):
            Matriz_info.loc[df.loc[line,'results']['ticker'],'description']=df.loc[line,'results']['description']
            Matriz_info.loc[df.loc[line,'results']['ticker'],'geography']=df.loc[line,'results']['geography']
            Matriz_info.loc[df.loc[line,'results']['ticker'],'dataset']=df.loc[line,'results']['dataset']
            Matriz_info.loc[df.loc[line,'results']['ticker'],'frequency']=df.loc[line,'results']['frequency']
            aux=pandas.DataFrame.from_dict(df.loc[line,'results']['data'])
            aux=aux.set_index(['dates'])
            aux.to_csv(df.loc[line,'results']['ticker']+'.csv')
    except:
          print("Algo Paso Pagina"+str(page))
    print(page)

Matriz_info.index.name='ticker'
Matriz_info.to_csv('aaainfo.csv')

