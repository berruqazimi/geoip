from django.test import TestCase

# Create your tests here.
import requests

def get_geoip_data(ip_address):
    url = f"https://json.geoiplookup.io/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

print(get_geoip_data('8.8.8.8'))