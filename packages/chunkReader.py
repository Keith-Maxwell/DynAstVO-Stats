import pandas as pd
import numpy as np


def concatenate(dfs):
    """Concatenate dataframes while preserving categorical columns.

    NB: We change the categories in-place for the input dataframes"""
    from pandas.api.types import union_categoricals
    import pandas as pd
    # Iterate on categorical columns common to all dfs
    for col in set.intersection(
        *[
            set(df.select_dtypes(include='category').columns)
            for df in dfs
        ]
    ):
        # Generate the union category across dfs for this column
        uc = union_categoricals([df[col] for df in dfs])
        # Change to union category for all dataframes
        for df in dfs:
            df[col] = pd.Categorical(df[col].values, categories=uc.categories)
    return pd.concat(dfs)


def _readChunk(file_name, cols, start, nrows):
    ''' Shortcut for calling the pandas.read_fwf() function'''
    return pd.read_fwf(file_name, header=None, names=list(cols.keys()), dtype=cols, skiprows=start, nrows=nrows)


def readByChunks(file_name, cols, nrows):
    ''' Reads the whole file by chunks of data in order to save RAM.
        - file_name : name of the file to read the data from.
        - cols : dictionary with name of the column and type of the data {"name":type}
        - nrows : number of rows per chunk.'''
    start = 0
    df = _readChunk(file_name, cols, start, nrows)  # read a first chunk of data
    while True:
        start += nrows  # offset the starting point to continue reading the file
        try:
            temp_df = pd.read_fwf(file_name, header=None, names=list(
                cols.keys()), dtype=cols, skiprows=start, nrows=nrows)
            df = concatenate([df, temp_df])  # append the new chunk to the full dataframe
        except pd.errors.EmptyDataError:  # there is nothing to read anymore
            break
    return df


if __name__ == "__main__":

    OScolnames = {'obs Type': 'category',
                  'measure Type': 'category',
                  'year': np.uint16,
                  'month': np.uint8,
                  'day': np.float64,
                  'RA': np.float64,
                  'DEC': np.float64,
                  'Obs Code': 'category',
                  'RA bias correction': np.float32,
                  'DEC bias correction': np.float32,
                  'RA precision': np.float64,
                  'DEC precision': np.float64,
                  'acceptance': 'bool',
                  'catalog': 'category',
                  'mag': np.float64,
                  'nbr obs': np.float16,
                  'random number': np.float64,
                  'RA delta': np.float64,
                  'DEC delta': np.float64,
                  'xhi square': np.float64,
                  'mag acceptance': np.float16,
                  'mag delta': np.float64,
                  'object number': 'category'}

    data = readByChunks('Data\\OpticalSpaceData.txt', OScolnames, 500)
    data.info()
