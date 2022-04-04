"""Script to compress the files downloaded from SECEX website."""

import argparse
import pathlib
import subprocess


def compress(path: str, dest_filepath: pathlib.Path):
    """Compress file or directory using 7z"""
    if dest_filepath.suffix != ".7z":
        dest_filepath = dest_filepath.with_suffix(".7z")
    if dest_filepath.exists():
        print(f"Skipping {dest_filepath}")
        return
    elif not dest_filepath.parent.exists():
        dest_filepath.parent.mkdir(parents=True)

    print(f"Compressing {path} to {dest_filepath}")

    command = [
        "7z",
        "a",
        "-t7z",
        "-m0=lzma2",
        "-mx=9",
        str(dest_filepath),
        path,
    ]
    print(command)

    subprocess.run(command)


def compress_auxiliary_tables(data_dirpath: pathlib.Path, dest_dirpath: pathlib.Path):
    """Compress auxiliary-tables directory using 7z"""
    dirpath = data_dirpath / "auxiliary-tables"
    compress(dirpath, dest_dirpath / "auxiliary-tables.7z")


def compress_csv_files(data_dirpath: pathlib.Path, dest_dirpath: pathlib.Path):
    """Compress CSV files in a directory using 7z"""
    datasets = ["exp", "imp", "exp-mun", "imp-mun", "exp-nbm", "imp-nbm", "repetro"]
    for dataset in datasets:
        for filepath in (data_dirpath / dataset).glob("*.csv"):
            dest_filepath = dest_dirpath / dataset / filepath.name
            compress(str(filepath), dest_filepath)


def get_parser():
    parser = argparse.ArgumentParser(
        description="Compress the files downloaded from SECEX website."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=pathlib.Path,
        required=True,
        help="The directory where the data is downloaded.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        required=True,
        help="The directory where the data will be downloaded.",
    )
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    compress_auxiliary_tables(args.input, args.output)
    compress_csv_files(args.input, args.output)


if __name__ == "__main__":
    main()
