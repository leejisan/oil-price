import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns
import matplotlib.colors as mcolors
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

class Oil:
    def __init__(self):
        self.data = self.temp_data = pd.read_csv('refined_data/data.csv', encoding='ansi')
        self.standard = ''
        self.do = ''
        self.sigungu = ''
        sns.set(font='Gulim', font_scale=1)
        plt.rcParams['figure.figsize'] = [16, 10]
        
    def set_columns(self,arr):
        self.temp_data = self.data[arr]
        
    def get_columns(self):
        return list(self.temp_data.columns)
        
    def set_standard(self,string):
        self.standard = string
        
    def get_standard(self):
        return self.standard     
    
    def set_do(self,string):
        self.do = string
        
    def get_do(self,string):
        return self.do
        
    def set_sigungu(self,string):
        self.sigungu = string
        
    def get_sigungu(self,string):
        return self.sigungu
    
    def cluster(self):
        kmeans = KMeans(n_clusters=3).fit(self.data[['경유','휘발유']].values)
        self.temp_data['클러스터'] = kmeans.labels_
        
    def elbow(self):
        X = self.temp_data[['경유','휘발유']].values
        sse = []
        for i in range(1,11):
            km = KMeans(n_clusters=i,algorithm='auto', random_state=42)
            km.fit(X)
            sse.append(km.inertia_)
        plt.plot(range(1,11), sse, marker='o')
        plt.xlabel('K')
        plt.ylabel('SSE')
        plt.show()

    def draw_plot(self):
        data = self.data[['기간','휘발유','경유','클러스터']]
        loc_array = list(data.groupby([self.standard]).groups.keys())[0:10]
        for i in loc_array:
            X = data.loc[data.groupby([self.standard]).groups[i]]
            X.reset_index(drop=True,inplace=True)
            for cluster in range(0,3):
                X = X[X['클러스터'] == cluster]
                X.reset_index(drop=True,inplace=True)
                plt.scatter(X[:]['경유'].astype(str),X[:]['휘발유'].astype(str),label=cluster, s=10)
                plt.xlabel('경유 가격(원)')
                plt.ylabel('휘발유 가격(원)')
                plt.title('하루간의 경유가격 분포')
                plt.grid(False)

    def show_plot(self):
        return plt.show()

if __name__ == "__main__":
    oil = Oil()
    oil.set_standard('기간')
    oil.draw_plot()
    oil.show_plot()