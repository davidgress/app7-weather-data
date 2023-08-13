import requests
API_KEY = "8d94efc882da2259cf76fdce33c2be37"


def get_data(place, forcast_days=None, kind=None):
    url = "http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&" \
          f"appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == "__main__":
    print(get_data(place='Tokyo'))