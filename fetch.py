import argparse
import pathlib
from datetime import date

import httpx

from comex_fetcher import fetcher, storage, tables

CURRENT_YEAR = date.today().year


def download_tables(data_dir: pathlib.Path, client: httpx.Client):
    for table in tables.AUX_TABLES:
        fetcher.table(table, data_dir, client)
    fetcher.tabelas_auxiliares(data_dir, client)


def download_trade(data_dir: pathlib.Path, client: httpx.Client):
    for dataset in tables.TRADE:
        start_year, end_year = tables.TRADE[dataset]["year_range"]
        if end_year is None:
            end_year = CURRENT_YEAR
        for year in range(start_year, end_year + 1):
            fetcher.trade(
                data_dir=data_dir,
                dataset=dataset,
                year=year,
                client=client,
            )


def download_trade_completa(data_dir: pathlib.Path, client: httpx.Client):
    for dataset in tables.ARQUIVO_UNICO:
        url = tables.get_url(dataset)
        metadata = fetcher.get_file_metadata(url)
        filepath = storage.get_trade_completa_filepath(
            dataset=dataset,
            modified=metadata["last_modified"],
        )
        if filepath.exists():
            continue
        fetcher.download_file(url, filepath, client)


def download_repetro(data_dir: pathlib.Path, client: httpx.Client):
    for dataset in tables.REPETRO_TABLES:
        fetcher.repetro(data_dir=data_dir, dataset=dataset, client=client)


def download_all(data_dir: pathlib.Path, client: httpx.Client):
    download_tables(data_dir, client)
    download_trade(data_dir, client)
    download_repetro(data_dir, client)


def get_parser():
    parser = argparse.ArgumentParser(
        description="Downloads the data from the SECEX website."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        help="The directory where the data will be downloaded.",
    )
    parser.add_argument(
        "dataset",
        choices=[
            "all",
            "tables",
            "trade",
            "trade-completa",
            "trade-mun",
            "trade-mun-completa",
            "trade-nbm",
            "repetro",
        ],
        help="The dataset to download.",
    )
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.output is None:
        args.output = pathlib.Path.cwd()
    with httpx.Client(verify=False) as client:
        match args.dataset:
            case "all":
                download_all(args.output, client)
            case "tables":
                download_tables(args.output, client)
            case "trade":
                download_trade(args.output, client)
            case "trade-completa":
                download_trade_completa(args.output, client)
            case "repetro":
                download_repetro(args.output, client)
            case _:
                parser.error(f"Unknown dataset: {args.dataset}")


if __name__ == "__main__":
    main()
