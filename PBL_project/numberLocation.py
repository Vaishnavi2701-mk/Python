import phonenumbers
import folium
from myNumber import number
from phonenumbers import geocoder

Key='c968fb85d4b146729eaa858ed9e5f49c'

dollNumber=phonenumbers.parse(number)
yourLocation=geocoder.description_for_number(dollNumber,"en")
print(yourLocation)

# get the service provider

from phonenumbers import carrier
service_provider=phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

# latitude and longitude

from opencage.geocoder import OpenCageGeocode

geocoder=OpenCageGeocode(Key)

query=str(yourLocation)
results=geocoder.geocode(query)
#print(results)

lat=results[0]['geometry']['lat']
lng=results[0]['geometry']['lng']

print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=yourLocation).add_to(myMap)

# save Map as html file

myMap.save("myLocation.html")

