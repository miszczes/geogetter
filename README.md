# GeoGetter

![GeoGetter Logo](https://github.com/miszczes/geogetter/assets/77160449/20ec6650-03cd-448a-99dd-4c7feeff40e0)<!-- Replace with a logo or banner image if desired -->

GeoGetter is a simple Python library and command-line tool that helps you retrieve geographic information for a given location using various APIs. Whether you need latitude and longitude coordinates, address details, or timezone information, GeoGetter has got you covered.

## Features

- Retrieve latitude and longitude coordinates for a location.
- Get detailed address information (country, city, postal code, etc.).
- Fetch timezone data for a specific location.
- Easy-to-use Python library with a command-line interface.

## GitHub repository

🔗 [geogetter GitHub repo](https://github.com/miszczes/geogetter) 

## Installation

You can install GeoGetter using pip (consider using venv):

```bash
pip install geogetter
```

## Using geogetter

```python
from geogetter import Geocoder

easter_island = Geocoder("Easter Island")

print(easter_island.lat, easter_island.lon)
```

Running this script should result in this output

```output
-27.1259451 -109.34963353785872
```

It's also possible to get more detailed information about the target
using following code:
```python
from geogetter import Geocoder

big_ben = Geocoder("Big Ben", address_json=True)

print(big_ben.target_name, "\n")

for item in big_ben.address_json:
    print(f"{item}: {big_ben.address_json.get(item)}")
```
This should result in the following std out:
```output
Big Ben, Bridge Street, Westminster, Millbank, City of Westminster, Greater London, England, SW1A 2JX, United Kingdom 

amenity: Big Ben
road: Bridge Street
quarter: Westminster
suburb: Millbank
city: City of Westminster
ISO3166-2-lvl8: GB-WSM
state_district: Greater London
state: England
ISO3166-2-lvl4: GB-ENG
postcode: SW1A 2JX
country: United Kingdom
country_code: gb
```


