# 旅行推銷員問題
## 題目解析
給一組城市和各城市之間的距離，求路過所有城市並回到起始城市的最短路徑。

## 由ChatGPT產生的結果
```
from typing import List
import math

def solve_tsp(distances: List[List[int]]) -> List[int]:
  # 记录当前所有可供选择的城市
  unvisited_cities = set(range(len(distances)))
  # 记录当前城市的编号
  current_city = 0
  # 记录已经访问过的城市的编号
  visited_cities = []
  
  while unvisited_cities:
    # 将当前城市加入已访问的城市列表中
    visited_cities.append(current_city)
    # 从未访问过的城市中移除当前城市
    unvisited_cities.remove(current_city)
    # 找到距离当前城市最近的城市
    nearest_city = None
    min_distance = math.inf
    for city in unvisited_cities:
      if distances[current_city][city] < min_distance:
        nearest_city = city
        min_distance = distances[current_city][city]
    # 将最近的城市设为下一个访问的城市
    current_city = nearest_city
  
  # 将起点加入已访问的城市列表中，结束旅行
  visited_cities.append(0)
  return visited_cities

```

理解並參考上面代碼原理後自己寫了一個

```
n = 4

S = [0] * n #用於存儲已訪問過的城市
D = [[0] * n for _ in range(n)] #用於存儲兩個城市之間的距離

sum = 0 #用於記算已訪問過的城市的最小路徑長度
Dtemp = 0 #保證Dtemp比任意兩個城市之間的距離都大
flag = 0 #最為訪問的標誌，若被訪問過則為1，從未被訪問過則為0

i = 1 #i是至今已访问过的城市
S[0] = 0
D[0][1] = 2
D[0][2] = 6
D[0][3] = 5
D[1][0] = 2
D[1][2] = 4
D[1][3] = 4
D[2][0] = 6
D[2][1] = 4
D[2][3] = 2
D[3][0] = 5
D[3][1] = 4
D[3][2] = 2

while i < n:
    k = 1
    Dtemp = 10000
    while k < n:
        l = 0
        flag = 0
        while l < i:
            if S[l] == k: #判斷該城市是否已被訪問過，若被訪問過
                flag = 1 #則flag為1
                break #跳出循环，不参与距离的比较
            else:
                l += 1
        if flag == 0 and D[k][S[i - 1]] < Dtemp: #D[k][S[i - 1]]表示當前未被訪問的城市k與上一個已訪問過的城市i-1之間的距離
            j = k #j用於存儲已訪問過的城市k
            Dtemp = D[k][S[i - 1]] #Dtemp用於暫時存儲當前最小路徑的值
        k += 1
    S[i] = j #將已訪問過的城市j存入到S[i]中
    i += 1
    sum += Dtemp #求出各城市之間的最短距離，注意：在結束循環時，該旅行商尚未回到原出發的城市

sum += D[0][j] #D[0][j]為旅行商所在的最後一個城市與原出發的城市之間的距離

for j in range(n):
    print(j, end=' ') #輸出經過的城市的路徑
print("\n" + str(sum)) #求出最短路徑的值

```
以下是使用結果
```
0 1 2 3 
13
```
