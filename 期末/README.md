# 模拟退火算法解決旅行推銷員問題
## 題目解析
TSP問題（Traveling Salesman Problem，旅行商問題），由威廉哈密頓爵士和英國數學家克克曼T.P.Kirkman於19世紀初提出。問題描述如下：  

有若干個城市，任何兩個城市之間的距離都是確定的，現要求一旅行商從某城市出發必須經過每一個城市且只在一個城市逗留一次，最後回到出發的城市，問如何事先確定一條最短的線路已保證其旅行的費用最少？  

## 模擬退火算法（Simulate Annealing Arithmetic，SAA）
### 什麼是模擬退火算法(簡介)  
模擬退火算法（Simulate Annealing Arithmetic，SAA）是一種通用概率演算法，用來在一個大的搜尋空間內找尋命題的最優解。它是基於Monte-Carlo迭代求解策略的一種隨機尋優算法。  

模擬退火算法是S.Kirkpatrick, C.D.Gelatt和M.P.Vecchi等人在1983年發明的，1985年，V.Černý也獨立發明了此演算法。模擬退火算法是解決TSP問題的有效方法之一。  

### 模擬退火算法的來源  
模擬退火算法來源於固體退火原理。  

物理退火: 將材料加熱後再經特定速率冷卻，目的是增大晶粒的體積，並且減少晶格中的缺陷。材料中的原子原來會停留在使內能有局部最小值的位置，加熱使能量變大，原子會離開原來位置，而隨機在其他位置中移動。退火冷卻時速度較慢，使得原子有較多可能可以找到內能比原先更低的位置。  

模擬退火: 其原理也和固體退火的原理近似。模擬退火算法從某一較高初溫出發，伴隨溫度參數的不斷下降,結合概率突跳特性在解空間中隨機尋找目標函數的全局最優解，即在局部最優解能概率性地跳出並最終趨於全局最優。  

### 模擬退火算法  
爬山法是完完全全的貪心法，這種貪心是很鼠目寸光的，只把眼光放在局部最優解上，因此只能搜索到局部的最優值。模擬退火其實也是一種貪心算法，只不過與爬山法不同的是，模擬退火算法在搜索過程引入了隨機因素。模擬退火算法以一定的概率來接受一個比當前解要差的解，因此有可能會跳出這個局部的最優解，達到全局的最優解。  

### 使用模擬退火算法解決旅行商問題  
旅行商問題屬於所謂的NP完全問題。精確的解決TSP只能通過窮舉所有的路徑組合，其時間複雜度是O(N!) 。而使用模擬退火算法則可以較快速算法一條近似的最優路徑。大體的思路如下：  

1.產生一條新的遍歷路徑P(i+1)，計算路徑P(i+1)的長度L( P(i+1) )   
2.若L(P(i+1)) < L(P(i))，則接受P(i+1)為新的路徑，否則以模擬退火的那個概率接受P(i+1) ，然後降溫   
3.重複步驟1，2直到滿足退出條件  
  
  
以下為ChatGPT以模拟退火算法解決此問題的程式碼，我大概理解其原理。   

## 由ChatGPT產生的結果  
```
import numpy as np
import math

def simulated_annealing(cities, Tmax, Tmin, alpha):
    n = len(cities)
    current_solution = np.random.permutation(n)
    best_solution = current_solution.copy()
    L = math.sqrt(n)
    T = Tmax
    while T > Tmin:
        i = np.random.randint(0, n)
        swap_solution = current_solution.copy()
        swap_solution[i], swap_solution[(i+1) % n] = swap_solution[(i+1) % n], swap_solution[i]
        current_energy = energy(current_solution, cities)
        swap_energy = energy(swap_solution, cities)
        delta_energy = swap_energy - current_energy
        if delta_energy > 0:
            current_solution = swap_solution.copy()
            if swap_energy < energy(best_solution, cities):
                best_solution = swap_solution.copy()
        else:
            p = np.exp(-delta_energy / (L * T))
            if np.random.rand() < p:
                current_solution = swap_solution.copy()
        T = T * alpha
    return best_solution

def energy(solution, cities):
    distance = 0
    for i in range(len(solution)):
        distance += euclidean(cities[solution[i-1]], cities[solution[i]])
    return distance

def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
```
以下是我理解完後去實際演練寫的  
```
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

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def path_len(arr):
    path = 0
    for i in range(N-1):
        index1 = arr[i]
        index2 = arr[i+1]
        path += distance(city_pos[index1-1], city_pos[index2-1])
    return path + distance(city_pos[arr[-1]-1], city_pos[arr[0]-1])

def create_new():
    pos1 = random.randint(0, N-1)
    pos2 = random.randint(0, N-1)
    city_list[pos1], city_list[pos2] = city_list[pos2], city_list[pos1]

T = T0
count = 0
while T > T_end:
    for i in range(L):
        city_list_copy = city_list.copy()
        create_new()
        f1 = path_len(city_list)
        f2 = path_len(city_list_copy)
        df = f1 - f2
        if df > 0:
            city_list = city_list_copy
        elif math.exp(df/T) > random.uniform(0, 1):
            city_list = city_list_copy
    T *= q
    count += 1
print(" -> ".join(str(city) for city in city_list))
print(f"Path length: {path_len(city_list)}")
print(f"Iteration count: {count}")
```

參考資料:   
[ChatGPT](https://openai.com/blog/chatgpt/)   
[維基百科](https://zh.wikipedia.org/zh-tw/%E7%8B%AC%E7%AB%8B%E9%9B%86)
