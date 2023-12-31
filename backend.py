import requests
API_KEY = "8d94efc882da2259cf76fdce33c2be37"


def get_data(place, forecast_days=None):
    url = "http://api.openweathermap.org/data/2.5/forecast?" \
          f"q={place}&" \
          f"appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]
    # if kind == "Temperature":
    #     filtered_data = [dict1["main"]["temp"] for dict1 in filtered_data]
    # if kind == "Sky":
    #     filtered_data = [dict1["weather"][0]["main"] for dict1 in filtered_data]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place='Tokyo', forecast_days=3))