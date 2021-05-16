# -*- coding: utf-8 -*-
"""
Created on Mon May  3 23:28:04 2021
@author: JOSECAL
"""
import geopandas as gpd
import rasterio
from rasterio.plot import show
from rasterio.plot import show_hist
import rasterstats
import matplotlib.pyplot as plt
import pandas as pd
# Read the shapefiles 
limite_estatal_baja = gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\03 Rainfall Baja\Shapes\Limite estatal\lim_est.shp')
ANP_Mexico = gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\00 Mexico\Shapes\ANP\anp2020gw\anp2020gw.shp')
cuencas_Mexico = gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\00 Mexico\Shapes\Cuencas\cue250k_07gw\cue250k_07gw.shp')
municipios_Mexico = gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\00 Mexico\Shapes\Municipios\mun20gw\mun20gw.shp')
rios_Mexico = gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\00 Mexico\Shapes\Rios\hidro4mgw\hidro4mgw.shp')
vias_Mexico = gpd.read_file(r'C:\Users\josecal\Documents\GEO-PROYECTOS\00 Mexico\Shapes\Vias\viassct012gw\viassct012gw.shp')
# Plot the shapefiles 
limite_estatal_baja.plot()
ANP_Mexico.plot()
cuencas_Mexico.plot()
municipios_Mexico.plot()
rios_Mexico.plot()
vias_Mexico.plot()
# Read the raster TIF
rainfall_baja = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\03 Rainfall Baja\Raster\baja_prec_10.tif', mode = 'r')
show(rainfall_baja)
rainfall_baja_1 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_1.tif', mode = 'r')
show(rainfall_baja_1)
rainfall_baja_2 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_2.tif', mode = 'r')
show(rainfall_baja_2)
rainfall_baja_3 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_3.tif', mode = 'r')
show(rainfall_baja_3)
rainfall_baja_4 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_4.tif', mode = 'r')
show(rainfall_baja_4)
rainfall_baja_5 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_5.tif', mode = 'r')
show(rainfall_baja_5)
rainfall_baja_6 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_6.tif', mode = 'r')
show(rainfall_baja_6)
rainfall_baja_7 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_7.tif', mode = 'r')
show(rainfall_baja_7)
rainfall_baja_8 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_8.tif', mode = 'r')
show(rainfall_baja_8)
rainfall_baja_9 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_9.tif', mode = 'r')
show(rainfall_baja_9)
rainfall_baja_10 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_10.tif', mode = 'r')
show(rainfall_baja_10)
rainfall_baja_11 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_11.tif', mode = 'r')
show(rainfall_baja_11)
rainfall_baja_12 = rasterio.open(r'C:\Users\josecal\Documents\GEO-PROYECTOS\04 Rainfall 1902_2015\Raster\prec_1902_2015\baja_prec_12.tif', mode = 'r')
show(rainfall_baja_12)
# Plotting the raster rainfall and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja, ax = ax1, title = 'Rainfall')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja, title = 'Histogram Rainfall', ax = ax2)
plt.show()
# Plotting the raster rainfall_1 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_1, ax = ax1, title = 'Rainfall_January')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_1, title = 'Histogram Rainfall_January', ax = ax2)
plt.show()
# Plotting the raster rainfall_2 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_2, ax = ax1, title = 'Rainfall_February')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_2, title = 'Histogram Rainfall_February', ax = ax2)
plt.show()
# Plotting the raster rainfall_3 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_3, ax = ax1, title = 'Rainfall_March')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_3, title = 'Histogram Rainfall_March', ax = ax2)
plt.show()
# Plotting the raster rainfall_4 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_4, ax = ax1, title = 'Rainfall_April')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_4, title = 'Histogram Rainfall_April', ax = ax2)
plt.show()
# Plotting the raster rainfall_5 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_5, ax = ax1, title = 'Rainfall_May')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_5, title = 'Histogram Rainfall_May', ax = ax2)
plt.show()
# Plotting the raster rainfall_6 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_6, ax = ax1, title = 'Rainfall_June')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_6, title = 'Histogram Rainfall_June', ax = ax2)
plt.show()
# Plotting the raster rainfall_7 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_7, ax = ax1, title = 'Rainfall_July')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_7, title = 'Histogram Rainfall_July', ax = ax2)
plt.show()
# Plotting the raster rainfall_8 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_8, ax = ax1, title = 'Rainfall_August')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_8, title = 'Histogram Rainfall_August', ax = ax2)
plt.show()
# Plotting the raster 9 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_9, ax = ax1, title = 'Rainfall_September')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_9, title = 'Histogram Rainfall_September', ax = ax2)
plt.show()
# Plotting the raster rainfall_10 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_10, ax = ax1, title = 'Rainfall_Octubre')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_10, title = 'Histogram Rainfall_Octubre', ax = ax2)
plt.show()
# Plotting the raster rainfall_11 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_11, ax = ax1, title = 'Rainfall_November')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_11, title = 'Histogram Rainfall_November', ax = ax2)
plt.show()
# Plotting the raster rainfall_12 and the districts shapefile together 
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (20,8))
show(rainfall_baja_12, ax = ax1, title = 'Rainfall_December')
limite_estatal_baja.plot(ax = ax1, facecolor = 'None', edgecolor = 'yellow', linewidth=4)
show_hist(rainfall_baja_12, title = 'Histogram Rainfall_December', ax = ax2)
plt.show()

#Ploting_histograms on one layer
fig, (ax1) = plt.subplots(figsize = (20,8))
show_hist(rainfall_baja_1, title = 'Histogram Rainfall', bins=50, lw=0.0, alpha=0.3, ax = ax1)
show_hist(rainfall_baja_2, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_3, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_4, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_5, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_6, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_7, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_8, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_9, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_10,title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_11, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
show_hist(rainfall_baja_12, title = 'Histogram Rainfall',bins=50, lw=0.0,alpha=0.3, ax = ax1)
plt.show()
plt.subplots?
       
# Clipping Baja shapefiles
ANP_Baja = gpd.clip(ANP_Mexico, limite_estatal_baja)
cuencas_Baja = gpd.clip(cuencas_Mexico, limite_estatal_baja)
municipios_Baja = gpd.clip(municipios_Mexico, limite_estatal_baja)
rios_Baja = gpd.clip(rios_Mexico, limite_estatal_baja)
vias_Baja = gpd.clip(vias_Mexico, limite_estatal_baja)
# Plot the clipped shapefiles 
ANP_Baja.plot()
cuencas_Baja.plot()
municipios_Baja.plot()
rios_Baja.plot()
vias_Baja.plot()

# Reprojecting GeoPandas GeoDataFrames
ANP_Baja_32611 = ANP_Baja.to_crs(epsg = 32611)
ANP_Baja_32611.plot()
cuencas_Baja_32611= cuencas_Baja.to_crs(epsg = 32611)
cuencas_Baja_32611.plot()
municipios_Baja_32611 = municipios_Baja.to_crs(epsg = 32611)
municipios_Baja_32611.plot()
rios_Baja_32611 = rios_Baja.to_crs(epsg = 32611)
rios_Baja_32611.plot()
vias_Baja_32611 = vias_Baja.to_crs(epsg = 32611)
vias_Baja_32611.plot()

# Plotting multiple layers1
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize = (40,20))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2, linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_1, ax = ax1, title = 'Rainfall January 1902-2015')

municipios_Baja.plot(ax = ax2, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax2, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax2, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax2, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax2, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax2, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_2, ax = ax2, title = 'Rainfall February 1902-2015')

municipios_Baja.plot(ax = ax3, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax3, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax3, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax3, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax3, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax3, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_3, ax = ax3, title = 'Rainfall March 1902-2015')

# Plotting multiple layers2
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize = (40,20))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_4, ax = ax1, title = 'Rainfall April 1902-2015')

municipios_Baja.plot(ax = ax2, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax2, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax2, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax2, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax2, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax2, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_5, ax = ax2, title = 'Rainfall May 1902-2015')

municipios_Baja.plot(ax = ax3, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax3, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax3, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax3, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax3, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax3, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_6, ax = ax3, title = 'Rainfall June 1902-2015')

# Plotting multiple layers3
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize = (40,20))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_7, ax = ax1, title = 'Rainfall July 1902-2015')

municipios_Baja.plot(ax = ax2, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax2, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax2, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax2, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax2, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax2, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_8, ax = ax2, title = 'Rainfall August 1902-2015')

municipios_Baja.plot(ax = ax3, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax3, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax3, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax3, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax3, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax3, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_9, ax = ax3, title = 'Rainfall September 1902-2015')

# Plotting multiple layers4
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize = (40,20))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_10, ax = ax1, title = 'Rainfall October 1902-2015')

municipios_Baja.plot(ax = ax2, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax2, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax2, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax2, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax2, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax2, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_11, ax = ax2, title = 'Rainfall Noviembre 1902-2015')

municipios_Baja.plot(ax = ax3, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax3, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax3, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax3, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax3, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax3, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_12, ax = ax3, title = 'Rainfall Diciembre 1902-2015')

# Plotting single layers
fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_1, ax = ax1, title = 'Rainfall January 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_2, ax = ax1, title = 'Rainfall February 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_3, ax = ax1, title = 'Rainfall March 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_4, ax = ax1, title = 'Rainfall April 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_5, ax = ax1, title = 'Rainfall May 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_6, ax = ax1, title = 'Rainfall June 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_7, ax = ax1, title = 'Rainfall July 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_8, ax = ax1, title = 'Rainfall August 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_9, ax = ax1, title = 'Rainfall September 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_10, ax = ax1, title = 'Rainfall October 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_11, ax = ax1, title = 'Rainfall November 1902-2015')

fig, (ax1) = plt.subplots(figsize = (20,10))
municipios_Baja.plot(ax = ax1, color = 'none', edgecolor = 'white', zorder=2,  linewidth=0.4)
limite_estatal_baja.plot(ax = ax1, color = 'none', edgecolor = 'red',zorder=6, linewidth=2)
vias_Baja.plot(ax = ax1, color = 'yellow',zorder=6, linewidth=0.2)
ANP_Baja.plot(ax = ax1, color = 'none', edgecolor = '#46FB14', zorder=3, linewidth=0.6)
rios_Baja.plot(ax = ax1, color = '#56BDDF', zorder=6, linewidth=2, alpha=0.4)
cuencas_Baja.plot(ax = ax1, color = 'none', edgecolor = '#0940F1', zorder=2, linewidth=0.7)
show(rainfall_baja_12, ax = ax1, title = 'Rainfall December 1902-2015')

















