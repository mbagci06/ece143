# -*- coding: utf-8 -*-
"""World_mp_plot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GNkFJfX50XJh5OyuIkERuOMhd0Fg4_xL
"""

plt.rcParams["figure.figsize"] = (20, 10)

from google.colab import files
uploaded = files.upload()

!pip install --upgrade geopandas
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import geopandas as gpd
import plotly.express as px
import pandas as pd
import folium
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

df = pd.read_csv('voter-turnout.csv')
print(df.columns)
table = pd.pivot_table(df,index=['Entity','Code'], columns=['Year'])
# print(table)


def f(x):
  if x.last_valid_index() is None:
    return np.nan
  else:
    return x[x.last_valid_index()]

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

# print(plt.colorbar(axs1))

# cbar = clf.collections[0].colorbar
# print(type(cbar))
# cbar.axs1.colorbar(labelsize=15)
# plt.colorbar(shrink=0.5)

# Locating current axes
# divider = make_axes_locatable(axs1)
  
# creating new axes on the right
# side of current axes(ax).
# The width of cax will be 5% of ax
# and the padding between cax and ax
# will be fixed at 0.05 inch.
# colorbar_axes = divider.append_axes("right",
                                    # size="5%",
                                    # pad=0.5)
# Using new axes for colorbar
# plt.colorbar(clf, cax=colorbar_axes)
# plt.figure(figsize=(10,10))

from google.colab import files
res = clf.get_figure()
res.savefig('world_map_cbar.pdf')
files.download("world_map_cbar.pdf")