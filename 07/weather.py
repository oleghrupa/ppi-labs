import requests
import json
import pandas as pd

def pretty_print(data: dict[any, any]) -> None:
    for k,v in data.items():
        if k == "hourly":
            df = pd.DataFrame(zip(v["time"], v["temperature_2m"]), columns=("time", "temp"))
            print(df)
        else:
            print(f"{k} => {v}")

def main() -> None:
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
            "latitude": 49.83,
            "longitude": 24.03,
            "hourly": "temperature_2m"
    }

    response = requests.get(url, params=params)
    data = json.loads(response.text)
    pretty_print(data)

if __name__ == "__main__":
    main()
