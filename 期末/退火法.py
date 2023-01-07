import random
import math

T0 = 50000.0 #初始溫度
T_end = 1e-8
q = 0.98 #退火係數
L = 1000 #每個溫度時的跌代次數
N = 31 #城市

city_list = [i+1 for i in range(N)] #用於存放解
#城市座標
city_pos = [
    (1304, 2312), (3639, 1315), (4177, 2244), (3712, 1399),
    (3488, 1535), (3326, 1556), (3238, 1229), (4196, 1004),
    (4312, 790), (4386, 570), (3007, 1970), (2562, 1756),
    (2788, 1491), (2381, 1676), (1332, 695), (3715, 1678),
    (3918, 2179), (4061, 2370), (3780, 2212), (3676, 2578),
    (4029, 2838), (4263, 2931), (3429, 1908), (3507, 2367),
    (3394, 2643), (3439, 3201), (2935, 3240), (3140, 3550),
    (2545, 2357), (2778, 2826), (2370, 2975)
]

def distance(city1, city2): #計算兩個城市的距離
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def path_len(arr): #路徑長
    path = 0
    for i in range(N-1):
        index1 = arr[i]
        index2 = arr[i+1]
        path += distance(city_pos[index1-1], city_pos[index2-1])
    return path + distance(city_pos[arr[-1]-1], city_pos[arr[0]-1])

def create_new(): #產生新解
    pos1 = random.randint(0, N-1)
    pos2 = random.randint(0, N-1)
    city_list[pos1], city_list[pos2] = city_list[pos2], city_list[pos1]

T = T0 #初始溫度
count = 0 #紀錄降溫次數
while T > T_end:
    for i in range(L):
        city_list_copy = city_list.copy()
        create_new()
        f1 = path_len(city_list) #初始解函式值
        f2 = path_len(city_list_copy) #新解值
        df = f1 - f2 #差值
        if df > 0:
            city_list = city_list_copy
        elif math.exp(df/T) > random.uniform(0, 1):
            city_list = city_list_copy
    T *= q #降溫
    count += 1
print(" -> ".join(str(city) for city in city_list)) #城市順序
print(f"Path length: {path_len(city_list)}") #最短路徑
print(f"Iteration count: {count}") #降火次數
