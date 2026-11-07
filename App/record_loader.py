import json
from pathlib import Path

from App.models import Record, convert_to_record


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "Data" / "raw" / "api_tasks.json"


def load_api_records():

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    records = []

    for item in data:
        record = convert_to_record(item)
        records.append(record)

    return records


if __name__ == "__main__":

    records = load_api_records()

    print("Total Record Objects:", len(records))

    print("\nFirst 5 Records:")

    for record in records[:5]:
        print(record)
        