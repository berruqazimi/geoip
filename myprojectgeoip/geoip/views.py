from django.shortcuts import render
import requests

def get_geoip_data(ip_address):
    url = f"https://json.geoiplookup.io/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def home(request):
    if request.method == "POST":
        ip_address = request.POST["ip_address"]
        geoip_data = get_geoip_data(ip_address)
        return render(request, "search.html", {"geoip_data": geoip_data})
    return render(request, "search.html")
