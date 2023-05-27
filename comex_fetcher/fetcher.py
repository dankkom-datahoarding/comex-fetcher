"""Functions to download trade data and code tables"""


import datetime as dt
import time
from pathlib import Path

import httpx
from tqdm import tqdm

from .storage import (
    get_table_filepath,
    get_trade_completa_filepath,
    get_trade_filepath,
)
from .tables import get_url


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


def tabelas_auxiliares(dirpath: Path, client: httpx.Client):
    """Downloads tabelas-auxiliares file

    Parameters
    ----------
    dirpath: Path
        Destination path directory to save file
    """
    url = get_url("tabelas-auxiliares")
    metadata = get_file_metadata(url)
    filepath = get_table_filepath(
        data_dir=dirpath,
        table_name="tabelas-auxiliares",
        modified=metadata["last_modified"],
        file_extension="xlsx",
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def exp(year: int, data_dir: Path, client: httpx.Client):
    """Downloads exp file

    Parameters
    ----------
    year: int
        exp year to download
    data_dir: Path
        Destination path directory to save file
    """
    url = get_url("exp", year=year)
    metadata = get_file_metadata(url)
    filepath = get_trade_filepath(
        data_dir=data_dir,
        dataset="exp",
        year=year,
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def imp(year: int, data_dir: Path, client: httpx.Client):
    """Downloads imp file

    Parameters
    ----------
    year: int
        imp year to download
    data_dir: Path
        Destination path directory to save file
    """
    url = get_url("imp", year=year)
    metadata = get_file_metadata(url)
    filepath = get_trade_filepath(
        data_dir=data_dir,
        dataset="imp",
        year=year,
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def exp_mun(year: int, data_dir: Path, client: httpx.Client):
    """Downloads exp-mun file

    Parameters
    ----------
    year: int
        exp_mun year to download
    data_dir: Path
        Destination path directory to save file
    """
    url = get_url("exp-mun", year=year)
    metadata = get_file_metadata(url)
    filepath = get_trade_filepath(
        data_dir=data_dir,
        dataset="exp-mun",
        year=year,
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def imp_mun(year: int, data_dir: Path, client: httpx.Client):
    """Downloads imp-mun file

    Parameters
    ----------
    year: int
        imp_mun year to download
    data_dir: Path
        Destination path directory to save file
    """
    url = get_url("imp-mun", year=year)
    metadata = get_file_metadata(url)
    filepath = get_trade_filepath(
        data_dir=data_dir,
        dataset="imp-mun",
        year=year,
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def exp_nbm(year: int, data_dir: Path, client: httpx.Client):
    """Downloads exp-nbm file

    Parameters
    ----------
    year: int
        exp_nbm year to download
    data_dir: Path
        Destination path directory to save file
    """
    url = get_url("exp-nbm", year=year)
    metadata = get_file_metadata(url)
    filepath = get_trade_filepath(
        data_dir=data_dir,
        dataset="exp-nbm",
        year=year,
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def imp_nbm(year: int, data_dir: Path, client: httpx.Client):
    """Downloads imp-nbm file

    Parameters
    ----------
    year: int
        imp_nbm year to download
    data_dir: Path
        Destination path directory to save file
    """
    url = get_url("imp-nbm", year=year)
    metadata = get_file_metadata(url)
    filepath = get_trade_filepath(
        data_dir=data_dir,
        dataset="imp-nbm",
        year=year,
        modified=metadata["last_modified"],)
    if filepath.exists():
        return
    download_file(url, filepath, client)


def exp_completa(data_dir: Path, client: httpx.Client):
    """Downloads the file with complete data of exp-completa

    Parameters
    ----------
    data_dir : Path
        Destination path directory to save file
    """
    url = get_url("exp-completa")
    metadata = get_file_metadata(url)
    filepath = get_trade_completa_filepath(
        dataset="exp-completa",
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def imp_completa(data_dir: Path, client: httpx.Client):
    """Downloads the file with complete data of imp-completa

    Parameters
    ----------
    data_dir : Path
        Destination path directory to save file
    """
    url = get_url("imp-completa")
    metadata = get_file_metadata(url)
    filepath = get_trade_completa_filepath(
        dataset="imp-completa",
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def exp_mun_completa(data_dir: Path, client: httpx.Client):
    """Downloads the file with complete data of exp-mun-completa

    Parameters
    ----------
    data_dir : Path
        Destination path directory to save file
    """
    url = get_url("exp-mun-completa")
    metadata = get_file_metadata(url)
    filepath = get_trade_completa_filepath(
        dataset="exp-mun-completa",
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def imp_mun_completa(data_dir: Path, client: httpx.Client):
    """Downloads the file with complete data of imp-mun-completa

    Parameters
    ----------
    data_dir : Path
        Destination path directory to save file
    """
    url = get_url("imp-mun-completa")
    metadata = get_file_metadata(url)
    filepath = get_trade_completa_filepath(
        dataset="imp-mun-completa",
        modified=metadata["last_modified"],
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def exp_repetro(data_dir: Path, client: httpx.Client):
    """Downloads the file with complete data of exp_repetro

    Parameters
    ----------
    data_dir : Path
        Destination path directory to save file
    """
    url = get_url("exp-repetro")
    metadata = get_file_metadata(url)
    filepath = get_table_filepath(
        data_dir=data_dir,
        table_name="exp-repetro",
        modified=metadata["last_modified"],
        file_extension="xlsx",
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)


def imp_repetro(data_dir: Path, client: httpx.Client):
    """Downloads the file with complete data of imp_repetro

    Parameters
    ----------
    data_dir : Path
        Destination path directory to save file
    """
    url = get_url("imp-repetro")
    metadata = get_file_metadata(url)
    filepath = get_table_filepath(
        data_dir=data_dir,
        table_name="imp-repetro",
        modified=metadata["last_modified"],
        file_extension="xlsx",
    )
    if filepath.exists():
        return
    download_file(url, filepath, client)
