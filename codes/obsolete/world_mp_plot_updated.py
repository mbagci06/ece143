"""World_mp_plot.py

Plotting world map

author:  Joseph Kuo, Yiyang Zhang

Original file is located at
    https://colab.research.google.com/drive/1GNkFJfX50XJh5OyuIkERuOMhd0Fg4_xL
"""

# plt.rcParams["figure.figsize"] = (20, 10)
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import geopandas as gpd
import plotly.express as px
import pandas as pd
import folium
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable




def f(x):
  """
  helper function to extract the index
  """
  if x.last_valid_index() is None:
    return np.nan
  else:
    return x[x.last_valid_index()]



if __name__=="__main__":
  df = pd.read_csv('voter-turnout.csv')
  print(df.columns)
  table = pd.pivot_table(df,index=['Entity','Code'], columns=['Year'])
  # print(table)

  table['temp'] = table.apply(f,axis=1)
  df_new = table['temp']
  # print(df_new)

  countries = gpd.read_file(
                gpd.datasets.get_path("naturalearth_lowres"))
  countries['Code'] = countries['iso_a3']

  df_to_plot = pd.merge(countries, df_new, on = 'Code')
  fig1, axs1 = plt.subplots(1,1)
  clf = df_to_plot.plot("temp", figsize=(20,20), cmap = "Blues", ax=axs1, legend = True, legend_kwds={"shrink":.8})
  clf.set_yticklabels([])
  clf.set_xticklabels([])
  plt.show()



  # from google.colab import files
  res = clf.get_figure()
  res.savefig('world_map_cbar.pdf')
  files.download("world_map_cbar.pdf")
  pass