"""
Very simple and lightweight geocoder using
OpenStreetMap Geocoding API - Nominatim

Version 0.1.0 (only forward geocoding)

@author Mikolaj S - my.doom
"""

import requests


class Geocoder:

    def __init__(self, address_details: str, address_json=False):
        """
        geogetter object instance creation

        :param address_details: Searched address details (could be just name of the city)
        :type address_details: str
        :param address_json: If true geogetter also fetches dictionary with a
        :type address_json: bool
        """
        coordinates = self.__use_nominatim_api(address_details, address_json)
        if address_json:
            self.target_name, self.lat, self.lon, self.address_json = coordinates
        else:
            self.target_name, self.lat, self.lon = coordinates

    @staticmethod
    def __use_nominatim_api(address_details: str, address_json: bool):
        """
        Requests call to use Nominatim API
        through address details with JSON response

        :param address_details: Searched address details (could be just name of the city)
        :type address_details: string
        :return: longitude and latitude of given determined address
        :rtype: str
        """
        _addr_dets = address_details.split(" ")
        response = requests.get(
            "https://nominatim.openstreetmap.org/search?addressdetails=1&q="
            + "+".join(_addr_dets)
            + "&format=jsonv2&limit=1",
            timeout=10
        )
        if response.status_code == 200:
            resp = dict(response.json()[0])
            result = [resp.get("display_name"), resp.get("lat"), resp.get("lon")]
            if address_json:
                result.append(resp.get("address"))
            return result
        else:
            raise ValueError(f"Status code: {response.status_code};"
                             " Could not connect to given http address")
