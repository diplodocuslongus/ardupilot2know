# the original file had improper header format (not matching the columns)
# and had end of lines with ,,,,,
# I used vi to delete all the ,,,
# :g/,,,/norm nD
# for the header, I added unknown,-1,0, in front of TimeUS so the header now looks like:
# unknown,-1,0,TimeUS,I,Status,GMS,GWk,NSats,HDop,Lat,Lng,Alt,Spd,GCrs,VZ,Yaw,U


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import utm

HOME = os.getenv("HOME")
PATH2FILES = f'{HOME}/Data/Drones/GPS/ITRI'
LOGNAME = 'gps_output_mod.csv'

data = pd.read_csv(PATH2FILES+'/'+LOGNAME)
# look only at the Lat and Lng columns
print(data[['Lat','Lng']].head())
lat_ary = data['Lat'].to_numpy()
lng_ary = data['Lng'].to_numpy()
print(f'latitutde numpy array: {lat_ary}')
print(f'longitude numpy array: {lng_ary}')
utm_out = utm.from_latlon(lat_ary, lng_ary)
print(len(utm_out))

x = utm_out[0]
y = utm_out[1]

# not sure what units are, with x being up to 60x10⁶
# it may be mm(???)
# in anycase, I scale (bias) all data by its min

x = x -np.min(x)
y = y -np.min(y)
fig,ax=plt.subplots(3)
ax[0].plot(x,y)
ax[1].plot(x)
ax[2].plot(y)
plt.show()
