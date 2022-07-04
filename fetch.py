import argparse
import pathlib
from datetime import date

from comex_fetcher import fetcher, tables

CURRENT_YEAR = date.today().year


def download_tables(destdir: pathlib.Path):
    for table in tables.AUX_TABLES:
        fetcher.table(table, destdir / "auxiliary-tables")
    fetcher.tabelas_auxiliares(destdir / "auxiliary-tables")


def download_trade(destdir: pathlib.Path):
    for year in range(1997, CURRENT_YEAR + 1):
        fetcher.exp(year, destdir / "exp")
        fetcher.imp(year, destdir / "imp")


def download_trade_completa(destdir: pathlib.Path):
    fetcher.exp_completa(destdir / "exp-completa")
    fetcher.imp_completa(destdir / "imp-completa")


def download_trade_mun(destdir: pathlib.Path):
    for year in range(1997, CURRENT_YEAR + 1):
        fetcher.exp_mun(year, destdir / "exp-mun")
        fetcher.imp_mun(year, destdir / "imp-mun")


def download_trade_mun_completa(destdir: pathlib.Path):
    fetcher.exp_mun_completa(destdir / "exp-mun-completa")
    fetcher.imp_mun_completa(destdir / "imp-mun-completa")


def download_trade_nbm(destdir: pathlib.Path):
    for year in range(1989, 1997):
        fetcher.exp_nbm(year, destdir / "exp-nbm")
        fetcher.imp_nbm(year, destdir / "imp-nbm")


def download_repetro(destdir: pathlib.Path):
    fetcher.exp_repetro(destdir / "exp-repetro")
    fetcher.imp_repetro(destdir / "imp-repetro")


def download_all(destdir: pathlib.Path):
    download_tables(destdir)
    download_trade(destdir)
    download_trade_mun(destdir)
    download_trade_nbm(destdir)
    download_repetro(destdir)


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
    match args.dataset:
        case "all":
            download_all(args.output)
        case "tables":
            download_tables(args.output)
        case "trade":
            download_trade(args.output)
        case "trade-completa":
            download_trade_completa(args.output)
        case "trade-mun":
            download_trade_mun(args.output)
        case "trade-mun-completa":
            download_trade_mun_completa(args.output)
        case "trade-nbm":
            download_trade_nbm(args.output)
        case "repetro":
            download_repetro(args.output)
        case _:
            parser.error(f"Unknown dataset: {args.dataset}")


if __name__ == "__main__":
    main()
