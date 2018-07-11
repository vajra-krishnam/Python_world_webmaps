import folium
import pandas

da=pandas.read_csv("simplemaps-worldcities-basic.csv")
latit=list(da["lat"])
longit=list(da["lng"])
c_name=list(da["city"])
tag=list(da["iso3"])
def get_the_color(ta):
    if ta=="IND":
        return 'orange'
    elif ta=="USA":
        return 'yellow'
    elif ta=="RUS":
        return 'blue'
    else:
        return 'red'
m=folium.Map(location=[17.41,78.48],zoom_start=6,tiles="Mapbox Bright")
gru=folium.FeatureGroup(name="My map")
for l1, l2, cn, ta in zip(latit,longit,c_name,tag):
     gru.add_child(folium.Marker(location=[l1,l2],popup=folium.Popup(str(cn),parse_html=True),icon=folium.Icon(color=get_the_color(ta))))
gru.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read())))
m.add_child(gru)
m.save("map3.html")
gru.add_child(folium.Marker(location=[19.41,78.48],popup="marker1",icon=folium.Icon(color='green')))
