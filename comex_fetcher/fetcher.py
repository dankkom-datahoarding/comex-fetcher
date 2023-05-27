"""Functions to download trade data and code tables"""


import datetime as dt
import time
from pathlib import Path

import httpx
from tqdm import tqdm

from .storage import (
    get_table_filepath,
    get_trade_unique_filepath,
    get_trade_filepath,
)
from .tables import ARQUIVO_UNICO, TOTAIS_PARA_VALIDACAO, get_url


def get_file_metadata(url):
    """Returns the metadata of a file

    Parameters
    ----------
    url: str
        The file's URL
    """
    r = httpx.head(url, verify=False)
    file_size = int(r.headers.get("Content-Length", 0))
    default_last_modified_string = "Thu, 01 Jan 1970 00:00:00 GMT"
    last_modified = dt.datetime.strptime(
        r.headers.get("Last-Modified", default_last_modified_string),
        "%a, %d %b %Y %H:%M:%S %Z",
    )
    return {
        "size": file_size,
        "last_modified": last_modified,
    }


def download_file(
    url: str,
    filepath: Path,
    client: httpx.Client,
    retry: int = 3,
    blocksize: int = 1024,
):
    """Downloads the file in `url` and saves it in `path`

    Parameters
    ----------
    url: str
        The resource's URL to download
    filepath: str
        The destination path of downloaded file
    client: httpx.Client
        Connection HTTP session
    retry: int [default=3]
        Number of retries until raising exception
    blocksize: int [default=1024]
        The block size of requests
    """

    print(f"Downloading {url}")

    if not filepath.parent.exists():
        filepath.parent.mkdir(parents=True)

    for x in range(retry):
        try:
            with client.stream("GET", url, timeout=300) as r:
                progress = tqdm(
                    total=int(r.headers.get("Content-Length", 0)),
                    unit="B",
                    unit_scale=True,
                    desc=filepath.name,
                )
                with open(filepath, "wb") as f:
                    for chunk in r.iter_bytes(blocksize):
                        f.write(chunk)
                        progress.update(len(chunk))
                progress.close()
                break
        except ConnectionError:
            time.sleep(3)
            if x == retry - 1:
                raise


def table(table_name: str, data_dir: Path, client: httpx.Client):
    """Downloads a table

    Parameters
    ----------
    table_name: str
        The name of the table to download
    data_dir: Path
        The data directory path of downloaded file
    """
    url = get_url(table_name)
    metadata = get_file_metadata(url)
    filepath = get_table_filepath(
        data_dir=data_dir,
        table_name=table_name,
        modified=metadata["last_modified"],
        file_extension="csv",
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def tabelas_auxiliares(data_dir: Path, client: httpx.Client):
    """Downloads tabelas-auxiliares file

    Parameters
    ----------
    data_dir: Path
        Destination path directory to save file
    """
    url = get_url("tabelas-auxiliares")
    metadata = get_file_metadata(url)
    filepath = get_table_filepath(
        data_dir=data_dir,
        table_name="tabelas-auxiliares",
        modified=metadata["last_modified"],
        file_extension="xlsx",
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def trade(data_dir: Path, dataset: str, year: int, client: httpx.Client):
    url = get_url(table=dataset, year=year)
    metadata = get_file_metadata(url)
    filepath = get_trade_filepath(
        data_dir=data_dir,
        dataset=dataset,
        year=year,
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def trade_unique(data_dir: Path, dataset: str, client: httpx.Client):
    """Downloads the file with complete data

    Parameters
    ----------
    data_dir : Path
        Destination path directory to save file
    """
    url = get_url(dataset)
    metadata = get_file_metadata(url)
    if dataset in TOTAIS_PARA_VALIDACAO:
        file_extension = "csv"
    elif dataset in ARQUIVO_UNICO:
        file_extension = "zip"
    filepath = get_trade_unique_filepath(
        data_dir=data_dir,
        dataset=dataset,
        modified=metadata["last_modified"],
        file_extension=file_extension,
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def repetro(data_dir: Path, dataset: str, client: httpx.Client):
    """Downloads the file with complete data of repetro

    Parameters
    ----------
    data_dir : Path
        Destination path directory to save file
    """
    url = get_url(dataset)
    metadata = get_file_metadata(url)
    filepath = get_table_filepath(
        data_dir=data_dir,
        table_name=dataset,
        modified=metadata["last_modified"],
        file_extension="xlsx",
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)
