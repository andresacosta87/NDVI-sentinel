#Análisis temporal Lote 1
ndvi1=eop1_s2.data['NDVI']
mask=eop1_s2.mask['IS_DATA']
time=np.array(eop1_s2.timestamp)
t, w, h, _ = ndvi1.shape 

ndvi_clean = ndvi.copy()
ndvi_clean[~mask] = np.nan # set values of invalid pixels to NaN'

ndvi_mean = np.nanmean(ndvi1.reshape(t, w * h).squeeze(), axis=1) 
ndvi_mean_clean = np.nanmean(ndvi_clean.reshape(t, w * h).squeeze(), axis=1)
time_clean = time[~np.isnan(ndvi_mean_clean)]
ndvi_mean_clean = ndvi_mean_clean[~np.isnan(ndvi_mean_clean)]

fig = plt.figure(figsize=(20,5))
plt.plot(time_clean, ndvi_mean_clean, 's-', label = 'Promedio NDVI con limpieza de nubes')
plt.plot(time, ndvi_mean, 'o-', label='Promedio NDVI sin limpieza de nubes')
plt.xlabel('Tiempo', fontsize=15)
plt.ylabel('Promedio NDVI', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

#Análisis temporal Lote 2
ndvi2=eop2_s2.data['NDVI']
mask=eop2_s2.mask['IS_DATA']
time=np.array(eop2_s2.timestamp)
t, w, h, _ = ndvi2.shape 

ndvi_clean = ndvi.copy()
ndvi_clean[~mask] = np.nan # set values of invalid pixels to NaN'

ndvi_mean = np.nanmean(ndvi2.reshape(t, w * h).squeeze(), axis=1) 
ndvi_mean_clean = np.nanmean(ndvi_clean.reshape(t, w * h).squeeze(), axis=1)
time_clean = time[~np.isnan(ndvi_mean_clean)]
ndvi_mean_clean = ndvi_mean_clean[~np.isnan(ndvi_mean_clean)]

fig = plt.figure(figsize=(20,5))
plt.plot(time_clean, ndvi_mean_clean, 's-', label = 'Promedio NDVI con limpieza de nubes')
plt.plot(time, ndvi_mean, 'o-', label='Promedio NDVI sin limpieza de nubes')
plt.xlabel('Tiempo', fontsize=15)
plt.ylabel('Promedio NDVI', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

plt.legend(loc=2, prop={'size': 15});

#Análisis temporal Lote 3
ndvi3=eop3_s2.data['NDVI']
mask=eop3_s2.mask['IS_DATA']
time=np.array(eop3_s2.timestamp)
t, w, h, _ = ndvi1.shape 

ndvi_clean = ndvi.copy()
ndvi_clean[~mask] = np.nan # set values of invalid pixels to NaN'

ndvi_mean = np.nanmean(ndvi3.reshape(t, w * h).squeeze(), axis=1) 
ndvi_mean_clean = np.nanmean(ndvi_clean.reshape(t, w * h).squeeze(), axis=1)
time_clean = time[~np.isnan(ndvi_mean_clean)]
ndvi_mean_clean = ndvi_mean_clean[~np.isnan(ndvi_mean_clean)]

fig = plt.figure(figsize=(20,5))
plt.plot(time_clean, ndvi_mean_clean, 's-', label = 'Promedio NDVI con limpieza de nubes')
plt.plot(time, ndvi_mean, 'o-', label='Promedio NDVI sin limpieza de nubes')
plt.xlabel('Tiempo', fontsize=15)
plt.ylabel('Promedio NDVI', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)


#Análisis temporal Lote 4
ndvi4=eop4_s2.data['NDVI']
mask=eop4_s2.mask['IS_DATA']
time=np.array(eop4_s2.timestamp)
t, w, h, _ = ndvi1.shape 

ndvi_clean = ndvi.copy()
ndvi_clean[~mask] = np.nan # set values of invalid pixels to NaN'

ndvi_mean = np.nanmean(ndvi4.reshape(t, w * h).squeeze(), axis=1) 
ndvi_mean_clean = np.nanmean(ndvi_clean.reshape(t, w * h).squeeze(), axis=1)
time_clean = time[~np.isnan(ndvi_mean_clean)]
ndvi_mean_clean = ndvi_mean_clean[~np.isnan(ndvi_mean_clean)]

fig = plt.figure(figsize=(20,5))
plt.plot(time_clean, ndvi_mean_clean, 's-', label = 'Promedio NDVI con limpieza de nubes')
plt.plot(time, ndvi_mean, 'o-', label='Promedio NDVI sin limpieza de nubes')
plt.xlabel('Tiempo', fontsize=15)
plt.ylabel('Promedio NDVI', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)


#Análisis temporal Lote 5
ndvi5=eop5_s2.data['NDVI']
mask=eop5_s2.mask['IS_DATA']
time=np.array(eop5_s2.timestamp)
t, w, h, _ = ndvi5.shape 

ndvi_clean = ndvi.copy()
ndvi_clean[~mask] = np.nan # set values of invalid pixels to NaN'

ndvi_mean = np.nanmean(ndvi5.reshape(t, w * h).squeeze(), axis=1) 
ndvi_mean_clean = np.nanmean(ndvi_clean.reshape(t, w * h).squeeze(), axis=1)
time_clean = time[~np.isnan(ndvi_mean_clean)]
ndvi_mean_clean = ndvi_mean_clean[~np.isnan(ndvi_mean_clean)]

fig = plt.figure(figsize=(20,5))
plt.plot(time_clean, ndvi_mean_clean, 's-', label = 'Promedio NDVI con limpieza de nubes')
plt.plot(time, ndvi_mean, 'o-', label='Promedio NDVI sin limpieza de nubes')
plt.xlabel('Tiempo', fontsize=15)
plt.ylabel('Promedio NDVI', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

#Análisis temporal Lote 6
ndvi1=eop1_s2.data['NDVI']
mask=eop1_s2.mask['IS_DATA']
time=np.array(eop1_s2.timestamp)
t, w, h, _ = ndvi1.shape 

ndvi_clean = ndvi.copy()
ndvi_clean[~mask] = np.nan # set values of invalid pixels to NaN'

ndvi_mean = np.nanmean(ndvi1.reshape(t, w * h).squeeze(), axis=1) 
ndvi_mean_clean = np.nanmean(ndvi_clean.reshape(t, w * h).squeeze(), axis=1)
time_clean = time[~np.isnan(ndvi_mean_clean)]
ndvi_mean_clean = ndvi_mean_clean[~np.isnan(ndvi_mean_clean)]

fig = plt.figure(figsize=(20,5))
plt.plot(time_clean, ndvi_mean_clean, 's-', label = 'Promedio NDVI con limpieza de nubes')
plt.plot(time, ndvi_mean, 'o-', label='Promedio NDVI sin limpieza de nubes')
plt.xlabel('Tiempo', fontsize=15)
plt.ylabel('Promedio NDVI', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)