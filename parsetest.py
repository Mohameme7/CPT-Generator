import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from colorgen import ColorToolApp
from parsecpt import create_colormap, parse_cpt_string

cmap = ColorToolApp()
cmap.mainloop()

file_path = '2m_temperature_2024_07.nc'
dataset = xr.open_dataset(file_path)
time_index = 0
temperature = dataset['t2m'][time_index, :, :] - 273.15

lat = temperature.coords['latitude'].values
lon = temperature.coords['longitude'].values

plt.figure(figsize=(12, 6))

cpt_colors = parse_cpt_string(cmap.__str__())
colormap = create_colormap(cpt_colors)
ax = plt.axes(projection=ccrs.PlateCarree())
temperature.plot(ax=ax, transform=ccrs.PlateCarree(), cmap=colormap, cbar_kwargs={'label': '2m Temperature (°C)'})
ax.coastlines()
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.LAND, edgecolor='black')
ax.add_feature(cfeature.OCEAN)
gl = ax.gridlines(draw_labels=True)
gl.top_labels = False
gl.right_labels = False
plt.title(f'2m Temperature on {str(temperature.coords["time"].values)}')
plt.show()
