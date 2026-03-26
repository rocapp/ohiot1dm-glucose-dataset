#!/usr/bin/env python

"""convert2pfun.py"""

from data_processor_loader import DataLoader, OhioT1DMDataset
from pathlib import Path


def load_data(
    data_folders: Optional[List[str | os.PathLike]] = None, nsize: Optional[int] = 100
):
    if data_folders is None:
        data_folders = [p for p in Path("Ohio Data/").rglob("*/*")]
        print("Ohio Data folders:\n", data_folders)
    ds = OhioT1DMDataset(data_folders, nsize)
    return ds


def main():
    ds = load_data()
    df0 = ds.preprocessed_dfs[0]
    print(df0.to_markdown())


if __name__ == "__main__":
    main()
