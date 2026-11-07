import csv
import json
import logging

from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

RAW_FILE = BASE_DIR / "Data" / "raw" / "tasks.csv"

OUTPUT_FILE = BASE_DIR / "Data" / "records.json"

# Configure logging
logging.basicConfig(
    filename=BASE_DIR / "mindmate.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def validate_record(record):
    """Validate productivity task records."""

    required_fields = [
        "id",
        "title",
        "category",
        "priority",
        "status"
    ]

    for field in required_fields:

        if not record.get(field, "").strip():
            raise ValueError(f"Missing field: {field}")

    if record["priority"] not in ["Low", "Medium", "High"]:
        raise ValueError("Invalid priority")

    if record["status"] not in ["Pending", "In Progress", "Completed"]:
        raise ValueError("Invalid status")

    int(record["id"])

    return True


def clean_record(record):
    """Clean and standardize task information."""

    return {
        "id": int(record["id"].strip()),
        "title": record["title"].strip(),
        "category": record["category"].strip(),
        "priority": record["priority"].strip(),
        "status": record["status"].strip(),
        "due_date": record.get("due_date", "").strip()
    }


def ingest_data():

    cleaned_records = []

    try:

        if not RAW_FILE.exists():
            raise FileNotFoundError("Raw CSV file not found.")

        with RAW_FILE.open("r", encoding="utf-8", newline="") as file:

            reader = csv.DictReader(file)

            for row_number, row in enumerate(reader, start=2):

                try:
                    validate_record(row)

                    cleaned = clean_record(row)

                    cleaned_records.append(cleaned)

                except (ValueError, AttributeError) as error:

                    logging.warning(
                        "Skipping row %s: %s",
                        row_number,
                        error
                    )

        OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

        with OUTPUT_FILE.open("w", encoding="utf-8") as file:

            json.dump(cleaned_records, file, indent=4)

        logging.info(
            "Successfully ingested %s records.",
            len(cleaned_records)
        )

        print(f"Successfully processed {len(cleaned_records)} records.")

        print(f"JSON file saved at: {OUTPUT_FILE}")

    except FileNotFoundError as error:

        logging.error(str(error))

        print("Error:", error)

    except (OSError, csv.Error) as error:

        logging.exception("Data ingestion failed.")

        print("Data ingestion error:", error)


if __name__ == "__main__":
    ingest_data()