import folium
import webbrowser

# Create a Folium map object centered at specific coordinates
m = folium.Map(location=[47.365, 8.548], tiles="Cartodb Dark_Matter", zoom_start=13)

# Add a marker to the map
# The marker is placed at the specified coordinates with a popup message
markers = [] # load some coordinates here, then access them via for-loop

folium.Marker([47.365, 8.548], popup="Arthouse Piccadilly").add_to(m)

m.save("first.html")
webbrowser.open("first.html")
