import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import seaborn as sns

class Oil:
    def __init__(self):
        self.data = pd.read_csv('refined_data/data.csv', encoding='ansi')
        self.standard = ''
        self.do = ''
        self.sigungu = ''
        sns.set(font='Gulim', font_scale=1)
        
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
    
    def draw_plot(self):
        loc_array = list(self.data.groupby([self.standard]).groups.keys())
        X = self.data.loc[self.data.groupby([self.standard]).groups[loc_array[0]]]
        X.reset_index(drop=True,inplace=True)
        plt.scatter(X[:]['경유'],X[:]['휘발유'],c='black',label='충북', s=10)
        plt.xlabel('경유 가격(원)')
        plt.ylabel('휘발유 가격(원)')
        plt.title('기름값 분포')
        plt.grid(False)
        plt.legend()
            
    def show_plot(self):
        return plt.show()

if __name__ == "__main__":
    oil = Oil()
    oil.set_standard('기간')
    oil.draw_plot()
    oil.show_plot()