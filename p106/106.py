from gettext import npgettext
import numpy as np
import csv
import pandas as pd
import plotly.express as px

def getDataSource(data_path):
    marks=[]
    days=[]
    with open(data_path,newline='') as f:
        csvReader=csv.DictReader(f)
        for row in csvReader:
            marks.append(float(row['Marks In Percentage']))
            days.append(float(row['Days Present']))

    return {'x':marks,'y':days}

def findCorrelation(data_source):
    c=np.corrcoef(data_source['x'],data_source['y'])
    print("correlation between marks and days present",c[0,1])

def plotfigure(data_path):
    with open(data_path)as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Days Present",y="Marks In Percentage")    
        fig.show()

dataPath='data.csv'
dataSource=getDataSource(dataPath)
findCorrelation(dataSource)
plotfigure(dataPath)