"""Convert a two-column load manifest to JSON. Read CSV on standard input."""
import csv
import json
import sys


def convert(stream):
    reader = csv.DictReader(stream)
    if reader.fieldnames != ["load_id", "tons"]:
        raise ValueError("Expected the header load_id,tons")
    loads = {}
    for row in reader:
        identifier = (row["load_id"] or "").strip()
        tons = (row["tons"] or "").strip()
        if None in row or not identifier or identifier in loads:
            raise ValueError(f"Line {reader.line_num}: malformed or duplicate load")
        if not tons.isascii() or not tons.isdecimal() or int(tons) <= 0:
            raise ValueError(f"Line {reader.line_num}: expected positive whole tons")
        loads[identifier] = {"load_id": identifier, "tons": int(tons)}
    return list(loads.values())


if __name__ == "__main__":
    try:
        print(json.dumps(convert(sys.stdin), indent=2))
    except (ValueError, csv.Error) as error:
        sys.exit(str(error))
