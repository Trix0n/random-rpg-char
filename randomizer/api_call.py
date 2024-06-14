import requests


def api_call(data):
    url = "https://www.dnd5eapi.co/api/ability-scores/:index"

    headers = {
      'Accept': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    
    return response
