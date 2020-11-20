import pandas as pd
import numpy as np
import plotly.graph_objects as go
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
from plotly.offline import plot

class Oil:
    def __init__(self):
        self.data = pd.read_csv('refined_data/data.csv', encoding='ansi')
        self.standard = ''
        self.do = ''
        self.sigungu = ''
        
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
        kmeans = KMeans(n_clusters=3).fit(self.data[['휘발유','경유']].values)
        self.data['클러스터'] = kmeans.labels_
    
    def draw_plot(self):
        loc_array = list(self.data.groupby([self.standard]).groups.keys())
        fig = go.Figure()
        for i in range(0,5):
            X = self.data.loc[self.data.groupby([self.standard]).groups[loc_array[i]]]
            X.drop_duplicates(['경유','휘발유'],inplace=True)
            X.reset_index(drop=True,inplace=True)
            x = pd.to_datetime(X[:]['기간'], format='%Y%m%d')
            y = X[:]['경유']
            z = X[:]['휘발유']
            fig.add_trace(
                go.Scatter3d(x=x,y=y,z=z,marker=go.scatter3d.Marker(size=3),opacity=0.3,mode='markers')
            )
        plot(fig, filename='plotly-3d-scatter-small.html', auto_open=False)
            
    def show_plot(self):
        return fig.show()

if __name__ == "__main__":
    oil = Oil()
    oil.set_standard('기간')
    oil.draw_plot()