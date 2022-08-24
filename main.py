# %%
import csv
import os
import pandas as pd

# %%
df = pd.read_csv('臺北捷運每日分時各站OD流量統計資料_202207.csv') #檔案名稱
#母資料

# %%
df

# %%
date=[]
for i in range(1,32):
    if i <10: date.append('2022-07-0{}'.format(i)) #日期記得改
    else: date.append('2022-07-{}'.format(i))
date #獲取日期列表

# %%
stationa=df['進站']
stationa=list(set(list(stationa)))
stationa #獲取站點列表

# %%
def spli(station):
    path = station
    if not os.path.isdir(path):os.mkdir(path)
    if not os.path.isdir("{}/出站".format(path)):os.mkdir("{}/出站".format(path))
    if not os.path.isdir("{}/進站".format(path)):os.mkdir("{}/進站".format(path)) #建立資料夾
    def exit(x,y):
        a=(df[(df['{}'.format(x)] == station)]) #擷取資料
        for i in date:
            b=(a[(a['日期'] == i)]) #擷取日期
            b.reset_index(inplace = True,drop=True)
            data = pd.DataFrame(columns=stationa,index=list(range(24)))
            for j in stationa: #iterate站點時段：建立最後的dataframe
                c=(b[(b[y] == j)])
                c.set_index(["時段"], inplace = True)
                for k in range(24):
                    try: data.loc[k,j]=(c.loc[k]["人次"]) #賦值
                    except KeyError as err:pass #忽略空值
            data = data.rename_axis('time') #索引欄位命名
            data.to_csv("{}/{}/{}_{}.csv".format(path,x,i,x),encoding='Big5') #將dataframe匯出
    exit("進站","出站") #以進站為角度
    exit("出站","進站") #以出站為角度
# i 日期 j 站點 k 小時


# %%
spli("台北車站") #站點名稱 (可用for loop 跑整個台北捷運站)


