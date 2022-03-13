import plotly.figure_factory as mumpyff
import pandas as mumpyd

mumpyDat = mumpyd.read_csv("project108 - mumpy edition/mumpyData.csv")

mumpyData = mumpyDat["Avg Rating"].tolist() 

mumpyfig = mumpyff.create_distplot([mumpyData], ["concave lens"] , show_hist = False)

mumpyfig.show()






