import folium
from folium import plugins
from shapely.geometry import Polygon
from pyproj import Proj, Transformer, transform
import requests

# Provided data
zone_data = {
    "city": "Trivandrum",
    "zones": [
        {
            "id": 1,
            "name": "Vazhuthakadu",
            "boundary": [
                {"lat": 8.48194356780951, "lng": 77.0070377370972},
                {"lat": 8.516755099245186, "lng": 77.00754738921243},
                {"lat": 8.534949644028803, "lng": 76.97893384112379},
                {"lat": 8.518334877052531, "lng": 76.94982363968448},
                {"lat": 8.483535064071123, "lng": 76.94932077420053},
                {"lat": 8.465338299040226, "lng": 76.977921325508},
            ],
        },
        {
            "id": 2,
            "name": "Technopark",
            "boundary": [
                {"lat": 8.536518760511054, "lng": 76.92122609245942},
                {"lat": 8.571315161274914, "lng": 76.92172573938984},
                {"lat": 8.589486108702282, "lng": 76.89313121004591},
                {"lat": 8.572862922497226, "lng": 76.8640500616582},
                {"lat": 8.538078284352393, "lng": 76.8635571917395},
                {"lat": 8.51990506925161, "lng": 76.89213869519246},
            ],
        },
        {
            "id": 3,
            "name": "Chacka",
            "boundary": [
                {"lat": 8.483535064071123, "lng": 76.94932077420053},
                {"lat": 8.518334877052531, "lng": 76.94982363968448},
                {"lat": 8.536518760511054, "lng": 76.92122609245942},
                {"lat": 8.51990506925161, "lng": 76.89213869519246},
                {"lat": 8.485117002538091, "lng": 76.89164260835148},
                {"lat": 8.466930880263218, "lng": 76.92022714212546},
            ],
        },
        {
            "id": 4,
            "name": "Peroorkada",
            "boundary": [
                {"lat": 8.534949644028803, "lng": 76.97893384112379},
                {"lat": 8.569757779643906, "lng": 76.97944027307273},
                {"lat": 8.587939413992059, "lng": 76.95082971657575},
                {"lat": 8.571315161274914, "lng": 76.92172573938984},
                {"lat": 8.536518760511054, "lng": 76.92122609245942},
                {"lat": 8.518334877052531, "lng": 76.94982363968448},
            ],
        },
        {
            "id": 5,
            "name": "Kaniyapuram",
            "boundary": [
                {"lat": 8.589486108702282, "lng": 76.89313121004591},
                {"lat": 8.624279030340166, "lng": 76.89362763813648},
                {"lat": 8.642436987413335, "lng": 76.86503614046833},
                {"lat": 8.625804318831333, "lng": 76.8359612550223},
                {"lat": 8.5910231760842, "lng": 76.83547160230239},
                {"lat": 8.572862922497226, "lng": 76.8640500616582},
            ],
        },
         {
            "id": 5,
            "name": "Alappuzha Town",
            "boundary": [
                {"lat": 9.488462202837784,"lng": 76.35800321805853},
                {"lat": 9.523173773370845,"lng": 76.35843814058593},
                {"lat": 9.541091585477794,"lng": 76.32991682578766},
                {"lat": 9.524300628980985,"lng": 76.3009738527257},
                {"lat": 9.48960112843507,"lng": 76.30054566781097},
                {"lat": 9.471680514065769,"lng": 76.32905372043156},
            ],
            

         },
         {
            "id": 6,
            "name": "Paravoor",
            
            
            "boundary": [
                {"lat": 9.435814284802406,"lng": 76.38608968046117},
                {"lat": 9.47053047492161,"lng": 76.38652782417839},
                {"lat": 9.488462202837784,"lng": 76.35800321805853},
                {"lat": 9.471680514065769,"lng": 76.32905372043156},
                {"lat": 9.436976379090002,"lng": 76.32862231615206},
                {"lat": 9.419041877399508,"lng": 76.35713367214326},
            ],
            
            "id": 10,
            "name": "Manacaud",
            "boundary": [
                {"lat": 8.43053514082228,"lng": 76.97741524176146},
                {"lat": 8.465338299040226,"lng": 76.977921325508},
                {"lat": 8.483535064071123,"lng": 76.94932077420053},
                {"lat": 8.466930880263218,"lng": 76.92022714212546},
                {"lat": 8.432139451882794,"lng": 76.91972783864335},
                {"lat": 8.413940476908886,"lng": 76.94831538895816},
                
                ],
         },
    ],
}


# Create a Folium map centered around the first zone
map_center = [zone_data["zones"][0]["boundary"][0]["lat"], zone_data["zones"][0]["boundary"][0]["lng"]]
mymap = folium.Map(location=map_center, zoom_start=12)
h3_projection = Proj(proj='latlong', datum='WGS84')
osm_projection = Proj(proj='latlong', datum='WGS84')

# Project and add zone boundaries to the map using pyproj.Transformer
transformer = Transformer.from_proj(h3_projection, osm_projection)  # Create a Transformer instance

# FeatureGroup to hold the zones
zone_feature_group = folium.FeatureGroup(name='Zones')
mymap.add_child(zone_feature_group)

# Project and add zone boundaries to the map
for zone in zone_data["zones"]:
    boundary_coords = [(point["lat"], point["lng"]) for point in zone["boundary"]]
    osm_boundary_coords = [transform(h3_projection, osm_projection, lat, lng) for lat, lng in boundary_coords]
    polygon = Polygon(osm_boundary_coords)

    folium.Polygon(
        locations=polygon.exterior.coords[:],
        popup=zone["name"],
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.3,
    ).add_to(zone_feature_group)

# Add search functionality using Nominatim API
search_control = plugins.Search(
    layer=zone_feature_group,
    geom_type='Point',
    search_label='name',
    placeholder='Search for a location',
    collapsed=False,
    url='https://nominatim.openstreetmap.org/search?format=json&q={}',
)

# Save the map to an HTML file
mymap.save('zones_map_with_search.html')
