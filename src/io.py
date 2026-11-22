"""
Container of necessary input/output methods.

Reads the dataset file and validates its structure (although not its contents).
"""

import csv
from dataclasses import dataclass, fields
from pathlib import Path

DEFAULT_DATA_PATH = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "health_study_dataset.csv"
)


@dataclass(frozen=True)
class HealthRecord:
    """Health record structure, as expected from the given .csv file."""

    id: int
    age: int
    sex: str
    height: float
    weight: float
    systolic_bp: float
    cholesterol: float
    smoker: str
    disease: int


def read_csv(path: str | Path) -> list[list[str]]:
    """Read a UTF-8 CSV file, optionally with a BOM."""

    with Path(path).open(encoding="utf-8-sig", newline="") as file:
        return list(csv.reader(file, strict=True))


def import_health_study_dataset(
    path: str | Path = DEFAULT_DATA_PATH
) -> list[HealthRecord]:
    """Reads and validates the structure and numeric types of the dataset."""

    path = Path(path)
    rows = read_csv(path)

    if not rows:
        raise ValueError(f"{path} is empty")

    header, *data_rows = rows
    field_names = [field.name for field in fields(HealthRecord)]
    if len(header) != len(field_names) or set(header) != set(field_names):
        raise ValueError(f"{path}, CSV header: expected columns {', '.join(field_names)}")

    records = []
    for row_number, row in enumerate(data_rows, start=2):
        if len(row) != len(header):
            raise ValueError(
                f"{path}, CSV row {row_number}: expected "
                f"{len(header)} fields, found {len(row)}"
            )

        values = dict(zip(header, row))
        try:
            record = HealthRecord(
                id=int(values["id"]),
                age=int(values["age"]),
                sex=values["sex"],
                height=float(values["height"]),
                weight=float(values["weight"]),
                systolic_bp=float(values["systolic_bp"]),
                cholesterol=float(values["cholesterol"]),
                smoker=values["smoker"],
                disease=int(values["disease"]),
            )
        except ValueError as exc:
            raise ValueError(
                f"{path}, CSV row {row_number}: invalid numeric value: {exc}"
            ) from exc

        records.append(record)

    return records
