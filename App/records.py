from Data.sample_records import records as sample_data
# 1. Load all recordsCtrl + Shift + S
def load_records():
    """
    Load productivity records from the sample data file.
    """
    return sample_data


# 2. Search records using keyword

def search(records, keyword):
    """
    Search records using a keyword.
    """
    keyword = keyword.lower()

    results = []

    for record in records:

        for value in record.values():

            if keyword in str(value).lower():

                results.append(record)
                break

    return results


# 3. Count records by a particular field

def count_by(records, field):
    """
    Count records based on a given field.
    """
    counts = {}

    for record in records:

        value = record.get(field, "Unknown")

        counts[value] = counts.get(value, 0) + 1

    return counts


# 4. Find record using ID

def get_by_id(records, id):
    """
    Find a record using its unique ID.
    """
    for record in records:

        if record.get("id") == id:

            return record

    return None