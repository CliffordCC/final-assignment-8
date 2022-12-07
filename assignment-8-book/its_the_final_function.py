"""
Created on Mon Dec 16 09:38 2020

@author: Clifford Childs

"""

def custom_count_mean(data, grouping_col, string_name, mean_col):
    import pandas as pd
    """
    Given a dataframe, a column and string, return the count and mean of a specified string with said column
    
    Parameters
    ----------
    data : pandas.core.frame.DataFrame
        The dataframe to sample from
    string_name : str
        The string you want to count and find mean of
    mean_col : float
        The column you want to find the mean and count of
        
    Returns
    -------
    
        The mean value and count of a string contained within a column
        
    Raises
    ------
    TypeError
        If the input argument data is not of type pandas.core.frame.DataFrame
    AssertError
        If the input argument grouping_col is not in the data columns
    AssertError
        If the input argument action_col is not in the data columns
    TypeError
        If the string_name does on apper in the grouping_col
    
    Examples
    --------
    >>> custom_count_mean(movie_rev, 'voice_actor', 'Kristen Bell', 'inflation_adjusted_gross' )
    (1, 414997174.0)

    """
    
    # Checks if a dataframe is the type of object being passed into the data argument
    if not type(data) == pd.DataFrame: 
        raise TypeError("The data argument is not of type DataFrame")
    
    # Tests that the the grouping column is in the dataframe
    assert grouping_col in data.columns, "The grouping column does not exist in the dataframe"
    
    # Tests that the the mean_col column is in the dataframe
    assert mean_col in data.columns, "The mean column does not exist in the dataframe"
    
    #tests that the string_name in in the grouping_col
    if not data[grouping_col].str.contains(string_name).any():
        raise TypeError("The string_name does appear in grouping_col")
    
    # compute count
    count = data.groupby(grouping_col)[mean_col].count().reset_index().set_index(grouping_col).loc[string_name,mean_col]

    # compute mean
    mean = data.groupby(grouping_col)[mean_col].mean().reset_index().set_index(grouping_col).loc[string_name,mean_col]
    
    # return the result
    return(count, mean)
    