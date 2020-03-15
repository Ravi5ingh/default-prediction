###########################################################
# This file contains miscellaneous utility
###########################################################

import numpy as np

def experience_str2int(experience_string):
    """
    Converts the stringified experience into an int
    :param experience_string: The experience string
    :return:
    """

    swticher = {
        '< 1 year': 0,
        '1 year': 1,
        '2 years': 2,
        '3 years': 3,
        '4 years': 4,
        '5 years': 5,
        '6 years': 6,
        '7 years': 7,
        '8 years': 8,
        '9 years': 9,
        '10+ years': 10
    }

    return swticher.get(experience_string)

def reduce_mem_usage(df, verbose=True):
    """
    Takes a dataframe and returns one that takes less memory. This works by going over each column and representing
    it with the smallest possible data structure.
    Example usage: my_data = pd.read_csv('D:/SomeFile.csv').pipe(reduce_mem_usage)
    Source: (https://www.kaggle.com/arjanso/reducing-dataframe-memory-size-by-65)
    Parameters:
        df (DataFrame): The dataframe to optimize
        verbose (bool): Whether or not to be verbose about the operation
    """

    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
    start_mem = df.memory_usage().sum() / 1024 ** 2
    for col in df.columns:
        col_type = df[col].dtypes
        if col_type in numerics:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    df[col] = df[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    df[col] = df[col].astype(np.float32)
                else:
                    df[col] = df[col].astype(np.float64)
    end_mem = df.memory_usage().sum() / 1024 ** 2
    if verbose:
        print(
            "Mem. usage decreased to {:5.2f} Mb ({:.1f}% reduction)".format(
                end_mem, 100 * (start_mem - end_mem) / start_mem
            )
        )
    return df

def whats(thing) :
    """
    Prints the type of object passed in
    Parameters:
        thing (Object): The object for which the type needs to be printed
    """

    print(type(thing))

def row_count_of(df):
    """
    Get the row count of a dataframe
    :param df: The data frame
    :return: the count of rows
    """

    return len(df.index)

def pad(ser, result_len, default_val = np.nan):
    """
    Pad a Series with values at the end to make it the length provided. Default padding is NaN
    :param ser: The Series
    :param result_len: The resulting length. This should be more than the current length of the series
    :param default_val: The value to pad with
    :return: The padded Series
    """

    if ser.size > result_len:
        raise ValueError('Result length ' + str(result_len) + ' needs to be more than ' + str(ser.size))

    return ser.reset_index(drop=True).reindex(range(result_len), fill_value=default_val)

def is_nan(value):
    """
    Returns true if value is NaN, false otherwise
    Parameters:
         value (Object): An object to test
    """

    return value != value