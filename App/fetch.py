import requests

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "Data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

API_URL = "https://jsonplaceholder.typicode.com/todos"


def fetch_data():

    try:

        response = requests.get(API_URL, timeout=15)

        response.raise_for_status()

        records = response.json()

        output_file = RAW_DIR / "api_tasks.json"

        import json

        with output_file.open("w", encoding="utf-8") as file:
            json.dump(records, file, indent=4)

        print("Data downloaded successfully!")

        print("HTTP Status Code:", response.status_code)

        print("Total records downloaded:", len(records))

        print("Saved at:", output_file)

    except requests.exceptions.Timeout:

        print("Error: Request timed out.")

    except requests.exceptions.HTTPError as error:

        print("HTTP Error:", error)

    except requests.exceptions.RequestException as error:

        print("Request failed:", error)


if __name__ == "__main__":
    fetch_data()