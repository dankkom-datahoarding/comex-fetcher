"""Functions to download trade data and code tables"""


import datetime as dt
import pathlib
import time

import requests
import urllib3

from .tables import get_url

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_file_metadata(url):
    """Returns the metadata of a file

    Parameters
    ----------
    url: str
        The file's URL
    """
    r = requests.head(url, verify=False)
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


def download_file(url, filepath: pathlib.Path, retry=3, blocksize=1024):
    """Downloads the file in `url` and saves it in `path`

    Parameters
    ----------
    url: str
        The resource's URL to download
    filepath: str
        The destination path of downloaded file
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
            r = requests.get(url, verify=False)
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(blocksize):
                    f.write(chunk)
        except requests.exceptions.ConnectionError:
            time.sleep(3)
            if x == retry - 1:
                raise
        else:
            break


def table(table_name: str, dirpath: pathlib.Path):
    """Downloads a table

    Parameters
    ----------
    table_name: str
        The name of the table to download
    dirpath: pathlib.Path
        The destination path of downloaded file
    """
    url = get_url(table_name)
    metadata = get_file_metadata(url)
    filename = f"{table_name}_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def tabelas_auxiliares(dirpath: pathlib.Path):
    """Downloads tabelas-auxiliares file

    Parameters
    ----------
    dirpath: pathlib.Path
        Destination path directory to save file
    """
    url = get_url("tabelas-auxiliares")
    metadata = get_file_metadata(url)
    filename = f"tabelas-auxiliares_{metadata['last_modified']:%Y%m%d}.xlsx"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def exp(year: int, dirpath: pathlib.Path):
    """Downloads exp file

    Parameters
    ----------
    year: int
        exp year to download
    dirpath: pathlib.Path
        Destination path directory to save file
    """
    url = get_url("exp", year=year)
    metadata = get_file_metadata(url)
    filename = f"exp_{year}_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def imp(year: int, dirpath: pathlib.Path):
    """Downloads imp file

    Parameters
    ----------
    year: int
        imp year to download
    dirpath: pathlib.Path
        Destination path directory to save file
    """
    url = get_url("imp", year=year)
    metadata = get_file_metadata(url)
    filename = f"imp_{year}_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def exp_mun(year: int, dirpath: pathlib.Path):
    """Downloads exp-mun file

    Parameters
    ----------
    year: int
        exp_mun year to download
    dirpath: pathlib.Path
        Destination path directory to save file
    """
    url = get_url("exp-mun", year=year)
    metadata = get_file_metadata(url)
    filename = f"exp-mun_{year}_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def imp_mun(year: int, dirpath: pathlib.Path):
    """Downloads imp-mun file

    Parameters
    ----------
    year: int
        imp_mun year to download
    dirpath: pathlib.Path
        Destination path directory to save file
    """
    url = get_url("imp-mun", year=year)
    metadata = get_file_metadata(url)
    filename = f"imp-mun_{year}_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def exp_nbm(year: int, dirpath: pathlib.Path):
    """Downloads exp-nbm file

    Parameters
    ----------
    year: int
        exp_nbm year to download
    dirpath: pathlib.Path
        Destination path directory to save file
    """
    url = get_url("exp-nbm", year=year)
    metadata = get_file_metadata(url)
    filename = f"exp-nbm_{year}_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def imp_nbm(year: int, dirpath: pathlib.Path):
    """Downloads imp-nbm file

    Parameters
    ----------
    year: int
        imp_nbm year to download
    dirpath: pathlib.Path
        Destination path directory to save file
    """
    url = get_url("imp-nbm", year=year)
    metadata = get_file_metadata(url)
    filename = f"imp-nbm_{year}_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def exp_completa(dirpath: pathlib.Path):
    """Downloads the file with complete data of exp-completa

    Parameters
    ----------
    dirpath : pathlib.Path
        Destination path directory to save file
    """
    url = get_url("exp-completa")
    metadata = get_file_metadata(url)
    filename = f"exp-completa_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def imp_completa(dirpath: pathlib.Path):
    """Downloads the file with complete data of imp-completa

    Parameters
    ----------
    dirpath : pathlib.Path
        Destination path directory to save file
    """
    url = get_url("imp-completa")
    metadata = get_file_metadata(url)
    filename = f"imp-completa_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def exp_mun_completa(dirpath: pathlib.Path):
    """Downloads the file with complete data of exp-mun-completa

    Parameters
    ----------
    dirpath : pathlib.Path
        Destination path directory to save file
    """
    url = get_url("exp-mun-completa")
    metadata = get_file_metadata(url)
    filename = f"exp-mun-completa_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def imp_mun_completa(dirpath: pathlib.Path):
    """Downloads the file with complete data of imp-mun-completa

    Parameters
    ----------
    dirpath : pathlib.Path
        Destination path directory to save file
    """
    url = get_url("imp-mun-completa")
    metadata = get_file_metadata(url)
    filename = f"imp-mun-completa_{metadata['last_modified']:%Y%m%d}.csv"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def exp_repetro(dirpath: pathlib.Path):
    """Downloads the file with complete data of exp_repetro

    Parameters
    ----------
    dirpath : pathlib.Path
        Destination path directory to save file
    """
    url = get_url("exp-repetro")
    metadata = get_file_metadata(url)
    filename = f"exp-repetro_{metadata['last_modified']:%Y%m%d}.xlsx"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)


def imp_repetro(dirpath: pathlib.Path):
    """Downloads the file with complete data of imp_repetro

    Parameters
    ----------
    dirpath : pathlib.Path
        Destination path directory to save file
    """
    url = get_url("imp-repetro")
    metadata = get_file_metadata(url)
    filename = f"imp-repetro_{metadata['last_modified']:%Y%m%d}.xlsx"
    filepath = dirpath / filename
    if filepath.exists():
        return
    download_file(url, filepath)
