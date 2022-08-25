# mrt_OD_Data_arrangement
以python pandas基礎 切割、整理捷運每日每時OD資料
此REPO旨在協助整理捷運每日每時之opendata，將其整理，分割成小資料。
以下將對此repo的檔案做說明

## Main.py

python檔，整理母資料，將母資料分站、分時整理輸出成csv檔，裡面有逐行解釋，
NOTE：


    df = pd.read_csv('臺北捷運每日分時各站OD流量統計資料_202207.csv') #檔案名稱
此行放在目錄中，改成要分割的檔名！！

## 台北車站

輸出結果，分為進站與出站

## 臺北捷運每日分時各站OD流量統計資料.csv

母資料列表，針對自己需要的月份去下載
下載後再將該檔名打在py裡面。
NOTE：檔案很大，我推不上來，大約有九百萬行(300MB)

## 分析成果展示

### 放到GIS上
![Layout10](https://user-images.githubusercontent.com/101982224/186683658-7300fb56-6772-4426-8954-c85de0c2ec58.jpg)

### 在Excel上面繪製成平滑曲線圖
![image](https://user-images.githubusercontent.com/101982224/186683801-ac61b5d2-78df-46e3-8277-3ec3d02bb342.png)

### 將總流量排名視覺化
![image](https://user-images.githubusercontent.com/101982224/186683916-68e6a5e0-1c79-410a-aff6-1fe119d65270.png)

### 在上班時間分析住宅、商業區
![image](https://user-images.githubusercontent.com/101982224/186684104-24c9e25c-2a1e-41ed-9e86-46209d857672.png)

### 進出站人數相關性分析
![image](https://user-images.githubusercontent.com/101982224/186684242-67db0023-1f31-4d8d-bc04-35325497a69e.png)


