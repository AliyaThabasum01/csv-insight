import csv
import os


def analyze_csv(filename):
    if not os.path.isfile(filename):
        return None

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    columns = reader.fieldnames or []
    details = {}

    for column in columns:
        values = [row[column] for row in rows]

        missing = sum(
            1 for value in values
            if not value.strip()
        )

        numeric_values = []

        for value in values:
            try:
                numeric_values.append(float(value))
            except ValueError:
                pass

        info = {
            "type": "numeric" if numeric_values else "text",
            "missing": missing
        }

        if numeric_values:
            info["average"] = round(
                sum(numeric_values) / len(numeric_values), 2
            )

        details[column] = info

    return {
        "rows": len(rows),
        "columns": len(columns),
        "details": details
    }
