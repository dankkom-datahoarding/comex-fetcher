import argparse
from pathlib import Path

from comex_fetcher.storage import compress_data_dir


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o",
        "--data-dir",
        dest="data_dir",
        type=Path,
        required=True,
    )
    parser.add_argument(
        "-dest",
        dest="dest",
        type=Path,
        required=True,
    )
    args = parser.parse_args()

    compress_data_dir(args.data_dir, args.dest)


if __name__ == "__main__":
    main()
