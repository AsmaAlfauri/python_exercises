# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 12:33:46 2019

@author: Asma Alfauri
"""

import pandas as pd
import numpy as np
# =============================================================================
# #ex-1:
# data = [2,4,6,8,10]
# s = pd.Series(data)
# print('Series data :')
# print(s)
# =============================================================================

# =============================================================================
# #ex-2:
# d = {
#      'a':[100],
#      'b':[200],
#      'c':[300],
#      'd':[400],
#      'e':[800]
#      }
# df= pd.DataFrame(d)
# print(df)
# =============================================================================

# =============================================================================
# #ex-3:
# data=[20,10,150,110,100,50]
# df=pd.DataFrame(data)
# print( df.describe())
# df.plot(kind='bar')
# 
# =============================================================================

# =============================================================================
# #ex-4:
# d={
#    'd1':[100,200,5,400,700,100,200,50,400,700],
#    'd2':[140,0,300,400,200,140,0,700,400,200]
#    }
# 
# df=pd.DataFrame(d)
# df.plot()
# =============================================================================

# =============================================================================
# #ex-5:
# d={
#    'x':[78,85,96,80,86],
#    'y':[84,94,89,83,86],
#    'z':[86,97,96,72,83]
#    }
# df=pd.DataFrame(d)
# print(df)
# 
# =============================================================================

# =============================================================================
# #ex-6:
# names=(['Bob','Jessica','Mary','John','Mel'])
# births=([968,155,77,578,973])
# Series_n_b=pd.Series(births,index=names)
# print(Series_n_b)
# Series_n_b.plot.pie(y='births', figsize=(5, 5))
# 
# =============================================================================


# =============================================================================
#ex-7:
# d = [1,2,3,4,5,6,7,8,9]
# df= pd.DataFrame(d, columns = ['Number'])
# df.to_csv('myDataFrame.csv', sep='\t')
# df= pd.read_csv('myDataFrame.csv',sep='\t',index_col=0)
# print(df)
# 
# =============================================================================

# =============================================================================
# #ex-8:
# dates =pd.date_range('20000101', periods=4)
# df= pd.DataFrame(np.random.randn(4, 2), index=dates, columns=["A","B"])
# print(df)
# print(df.head(2))
# print(df[['A']])
# print(df[0:1]) 
# print(df['20000102':'20000104'])
# print(df.loc['20000102':'20000104', ["A"]])
# print(df.iloc[:,1:2])
# print(df[df>0])
# print(df[df.B>0])
# df["A"]=[100,200,300,100]
# print(df)
# print(df[df['A'].isin([200,300])])
# =============================================================================
























































