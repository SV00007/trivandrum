import folium
from folium import plugins
from shapely.geometry import Polygon
from pyproj import Proj, transform


# Provided data
zone_data = {
    "city": "Trivandrum",
    "zones": [
        {
            "id": 1,
            "name": "Vazhuthakadu",
            "uber_h3_index_3km": 605173824689799167,
            "boundary": [
                {
                    "lat": 8.48194356780951,
                    "lng": 77.0070377370972
                },
                {
                    "lat": 8.516755099245186,
                    "lng": 77.00754738921243
                },
                {
                    "lat": 8.534949644028803,
                    "lng": 76.97893384112379
                },
                {
                    "lat": 8.518334877052531,
                    "lng": 76.94982363968448
                },
                {
                    "lat": 8.483535064071123,
                    "lng": 76.94932077420053
                },
                {
                    "lat": 8.465338299040226,
                    "lng": 76.977921325508
                }
            ],
            "center_point": {
                "longitude": 76.97843078447107,
                "latitude": 8.50014275854123
            },
            "shifts": []
        },
        {
            "id": 3,
            "name": "Peroorkada",
            "uber_h3_index_3km": 605173820797485055,
            "boundary": [
                {
                    "lat": 8.534949644028803,
                    "lng": 76.97893384112379
                },
                {
                    "lat": 8.569757779643906,
                    "lng": 76.97944027307273
                },
                {
                    "lat": 8.587939413992059,
                    "lng": 76.95082971657575
                },
                {
                    "lat": 8.571315161274914,
                    "lng": 76.92172573938984
                },
                {
                    "lat": 8.536518760511054,
                    "lng": 76.92122609245942
                },
                {
                    "lat": 8.518334877052531,
                    "lng": 76.94982363968448
                }
            ],
            "center_point": {
                "longitude": 76.95032988371767,
                "latitude": 8.553135939417212
            },
            "shifts": []
        },
        {
            "id": 4,
            "name": "Technopark",
            "uber_h3_index_3km": 605173819992178687,
            "boundary": [
                {
                    "lat": 8.536518760511054,
                    "lng": 76.92122609245942
                },
                {
                    "lat": 8.571315161274914,
                    "lng": 76.92172573938984
                },
                {
                    "lat": 8.589486108702282,
                    "lng": 76.89313121004591
                },
                {
                    "lat": 8.572862922497226,
                    "lng": 76.8640500616582
                },
                {
                    "lat": 8.538078284352393,
                    "lng": 76.8635571917395
                },
                {
                    "lat": 8.51990506925161,
                    "lng": 76.89213869519246
                }
            ],
            "center_point": {
                "longitude": 76.8926381650809,
                "latitude": 8.55469438443158
            },
            "shifts": []
        },
        {
            "id": 2,
            "name": "Thampanoor",
            "uber_h3_index_3km": 605173820529049599,
            "boundary": [
                {
                    "lat": 8.483535064071123,
                    "lng": 76.94932077420053
                },
                {
                    "lat": 8.518334877052531,
                    "lng": 76.94982363968448
                },
                {
                    "lat": 8.536518760511054,
                    "lng": 76.92122609245942
                },
                {
                    "lat": 8.51990506925161,
                    "lng": 76.89213869519246
                },
                {
                    "lat": 8.485117002538091,
                    "lng": 76.89164260835148
                },
                {
                    "lat": 8.466930880263218,
                    "lng": 76.92022714212546
                }
            ],
            "center_point": {
                "longitude": 76.92072982533564,
                "latitude": 8.50172360894794
            },
            "shifts": []
        },
        {
            "id": 9,
            "name": "Kaniyapuram",
            "uber_h3_index_3km": 605173820394831871,
            "boundary": [
                {
                    "lat": 8.589486108702282,
                    "lng": 76.89313121004591
                },
                {
                    "lat": 8.624279030340166,
                    "lng": 76.89362763813648
                },
                {
                    "lat": 8.642436987413335,
                    "lng": 76.86503614046833
                },
                {
                    "lat": 8.625804318831333,
                    "lng": 76.8359612550223
                },
                {
                    "lat": 8.5910231760842,
                    "lng": 76.83547160230239
                },
                {
                    "lat": 8.572862922497226,
                    "lng": 76.8640500616582
                }
            ],
            "center_point": {
                "longitude": 76.86454631793895,
                "latitude": 8.607648757311424
            },
            "shifts": []
        },
        {
            "id": 10,
            "name": "Manacaud",
            "uber_h3_index_3km": 605173824421363711,
            "boundary": [
                {
                    "lat": 8.43053514082228,
                    "lng": 76.97741524176146
                },
                {
                    "lat": 8.465338299040226,
                    "lng": 76.977921325508
                },
                {
                    "lat": 8.483535064071123,
                    "lng": 76.94932077420053
                },
                {
                    "lat": 8.466930880263218,
                    "lng": 76.92022714212546
                },
                {
                    "lat": 8.432139451882794,
                    "lng": 76.91972783864335
                },
                {
                    "lat": 8.413940476908886,
                    "lng": 76.94831538895816
                }
            ],
            "center_point": {
                "longitude": 76.94882128519949,
                "latitude": 8.448736552164755
            },
            "shifts": []
        },
    ],
    "number_of_zones": 6
}




# Define the projection systems
h3_projection = Proj(proj='latlong', datum='WGS84')
osm_projection = Proj(proj='latlong', datum='WGS84')

# Create a Folium map centered around the first zone
map_center = [zone_data["zones"][0]["boundary"][0]["lat"], zone_data["zones"][0]["boundary"][0]["lng"]]
mymap = folium.Map(location=map_center, zoom_start=12)
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
    ).add_to(mymap)
# Save the map to an HTML file
mymap.save('index.html')