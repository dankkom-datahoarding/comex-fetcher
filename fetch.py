import argparse
import pathlib
from datetime import date

import httpx

from comex_fetcher import fetcher, tables

CURRENT_YEAR = date.today().year


def download_tables(data_dir: pathlib.Path, client: httpx.Client):
    for table in tables.AUX_TABLES:
        fetcher.table(table, data_dir, client)
    fetcher.tabelas_auxiliares(data_dir, client)


def download_trade(data_dir: pathlib.Path, client: httpx.Client):
    for year in range(1997, CURRENT_YEAR + 1):
        fetcher.exp(year, data_dir, client)
        fetcher.imp(year, data_dir, client)


def download_trade_completa(data_dir: pathlib.Path, client: httpx.Client):
    fetcher.exp_completa(data_dir, client)
    fetcher.imp_completa(data_dir, client)


def download_trade_mun(data_dir: pathlib.Path, client: httpx.Client):
    for year in range(1997, CURRENT_YEAR + 1):
        fetcher.exp_mun(year, data_dir, client)
        fetcher.imp_mun(year, data_dir, client)


def download_trade_mun_completa(data_dir: pathlib.Path, client: httpx.Client):
    fetcher.exp_mun_completa(data_dir, client)
    fetcher.imp_mun_completa(data_dir, client)


def download_trade_nbm(data_dir: pathlib.Path, client: httpx.Client):
    for year in range(1989, 1997):
        fetcher.exp_nbm(year, data_dir, client)
        fetcher.imp_nbm(year, data_dir, client)


def download_repetro(data_dir: pathlib.Path, client: httpx.Client):
    fetcher.exp_repetro(data_dir, client)
    fetcher.imp_repetro(data_dir, client)


def download_all(data_dir: pathlib.Path, client: httpx.Client):
    download_tables(data_dir, client)
    download_trade(data_dir, client)
    download_trade_mun(data_dir, client)
    download_trade_nbm(data_dir, client)
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
            case "trade-mun":
                download_trade_mun(args.output, client)
            case "trade-mun-completa":
                download_trade_mun_completa(args.output, client)
            case "trade-nbm":
                download_trade_nbm(args.output, client)
            case "repetro":
                download_repetro(args.output, client)
            case _:
                parser.error(f"Unknown dataset: {args.dataset}")


if __name__ == "__main__":
    main()
