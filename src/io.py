"""
Container of necessary input/output methods.

Reads the dataset file and validates its structure (although not its contents).
"""

import csv
from dataclasses import dataclass
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
    """Reads any CSV file and returns its contents."""

    with Path(path).open("r", encoding="utf-16") as file:
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

    records = []
    for row_number, row in enumerate(data_rows, start=2):
        if len(row) != len(header):
            raise ValueError(
                f"{path}, CSV row {row_number}: expected "
                f"{len(header)} fields, found {len(row)}"
            )

        if len(row) != 9:
            raise ValueError(
                f"{path}, CSV row {row_number}: expected "
                f"9 health record fields, found {len(row)}"
            )

        try:
            record = HealthRecord(
                id=int(row[0]),
                age=int(row[1]),
                sex=row[2],
                height=float(row[3]),
                weight=float(row[4]),
                systolic_bp=float(row[5]),
                cholesterol=float(row[6]),
                smoker=row[7],
                disease=int(row[8]),
            )
        except ValueError as exc:
            raise ValueError(
                f"{path}, CSV row {row_number}: invalid numeric value: {exc}"
            ) from exc

        records.append(record)

    return records
