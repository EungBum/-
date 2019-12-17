Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> import folium
>>> import webbrowser
>>> state_geo = ("c:/TL_SCCO_SIG_WGS84.json")
>>> state_unemployment = ("c:/Total_People_2019.csv")
>>> state_data = pd.read_csv(state_unemployment, encoding = 'euc-kr')
>>> m = folium.Map(location=[36, 127], tiles="OpenStreetMap", zoom_start=7)
>>> m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['Code', 'Population'],
 key_on='feature.properties.SIG_CD',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)

Warning (from warnings module):
  File "C:\Users\user\AppData\Local\Programs\Python\Python38-32\lib\site-packages\folium\folium.py", line 411
    warnings.warn(
FutureWarning: The choropleth  method has been deprecated. Instead use the new Choropleth class, which has the same arguments. See the example notebook 'GeoJSON_and_choropleth' for how to do this.
>>> m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=state_data,
 columns=['Code', 'Population'],
 key_on='feature.properties.SIG_CD',
 fill_color='YlGn',
 fill_opacity=0.7,
 line_opacity=0.5,
 legend_name='Population Rate (%)'
)
>>> folium.LayerControl().add_to(m)
<folium.map.LayerControl object at 0x0307D178>
>>> m.save("c:/크롤링과제")
>>> webbrowser.open_new("c:/크롤링과제")
