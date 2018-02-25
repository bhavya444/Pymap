import folium
import pandas as pd
map3 = folium.Map(location=[12.9716, 77.5946], zoom_start=15, tiles='OpenStreetMap')

df=pd.read_csv('localalities.txt')

for permalink,lon,lat in zip(df['permalink'],df['longitude'],df['latitude']):
    folium.Marker(location=[lat,lon],popup=permalink, icon=folium.Icon(color='red', icon_color='white')).add_to(map3)
print(map3.save('test3.html'))