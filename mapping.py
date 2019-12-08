import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('C:\\!DONOTDELETE\\devbin\\')
fp = 'C:\\!DONOTDELETE\\devbin\\gfsa000a11a_e\\gfsa000a11a_e.shp'
data = 'C:\\!DONOTDELETE\\devbin\\tenants.csv'
#merged_ON.columns ['PRUID', 'PRNAME', 'geometry', 'CLIENTS', 'PIF', 'GWP','EXPOSURE_CONTENTS']
var = 'PIF'
prov= 'Manitoba'

pd.set_option('display.max_columns',500)

map_df = gpd.read_file(fp)

map_df_ON = map_df[map_df.PRNAME==prov]
#map_df_AB = map_df[map_df.PRNAME=='Alberta']
#map_df_MB = map_df[map_df.PRNAME=='Manitoba']

df = pd.read_csv(data, header=0)

merged_ON = map_df_ON.set_index('CFSAUID').join(df.set_index('FSA'))
merged_ON = pd.merge(map_df_ON, df, left_on='CFSAUID', right_on='FSA', how='left')
merged_ON = merged_ON.fillna(0)


vmin=merged_ON[var].min()
vmax=merged_ON[var].max()

fig, ax = plt.subplots(1, figsize=(10,6))
ax.axis('off')

ax.set_title(str(prov)+' '+str(var))

sm = plt.cm.ScalarMappable(cmap='Blues',norm=plt.Normalize(vmin=vmin, vmax=vmax))
sm._A=[]
cbar = fig.colorbar(sm)
merged_ON.plot(column=var,cmap='Blues', linewidth=0.3, ax=ax, edgecolor='0.8')

#map_df_ON.plot()
plt.show()

