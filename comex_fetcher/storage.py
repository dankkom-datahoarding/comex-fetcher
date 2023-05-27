import datetime as dt
import subprocess
from pathlib import Path


def compress_data_dir(data_dir: Path, dest_dir: Path):
    for filepath in data_dir.glob("**/*"):
        if filepath.is_dir():
            continue
        print(filepath)
        dest_filename = filepath.name + ".7z"
        cmd = [
            "7z",
            "a",
            dest_dir / filepath.parent.relative_to(data_dir) / dest_filename,
            filepath,
        ]
        subprocess.run(cmd)


def get_trade_filepath(
    data_dir: Path,
    dataset: str,
    year: int,
    modified: dt.datetime,
) -> Path:
    filename = f"{dataset}_{year}_{modified:%Y%m%d}.csv"
    return data_dir / dataset / filename


def get_trade_unique_filepath(
    data_dir: Path,
    dataset: str,
    modified: dt.datetime,
    file_extension: str,
) -> Path:
    filename = f"{dataset}_{modified:%Y%m%d}.{file_extension}"
    return data_dir / dataset / filename


def get_table_filepath(
    data_dir: Path,
    table_name: str,
    modified: dt.datetime,
    file_extension: str,
) -> Path:
    filename = f"{table_name}_{modified:%Y%m%d}.{file_extension}"
    return data_dir / "auxiliary-tables" / filename
