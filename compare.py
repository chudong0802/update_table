import pandas as pd

def compare(path):
    #result.csv文件是之前去重后的文件夹
    data = pd.read_csv(path+'result.csv',encoding='utf-8')
    df1 = pd.DataFrame(data)
    new_data = pd.read_csv(path+'09-08.csv',encoding='utf-8',index_col=0)
    df2 = pd.DataFrame(new_data)
    # print(df2)
    # print(df2.index)
    num = []
    for i in range(len(df2['filename'])):
        for j in range(len(df1['filename'])):
            if df2['module'][i] == df1['module'][j] and df2['content'][i] == df1['content'][j]:
                num.append(i)
    df2.drop([i for i in num],inplace=True)
    df2.to_csv('./strictmode/0908_result.csv',index=0)
    # print(df2)
if __name__ == '__main__':
    compare('./strictmode/')
