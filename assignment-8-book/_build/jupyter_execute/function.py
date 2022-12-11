#!/usr/bin/env python
# coding: utf-8

# # Function and More exploration

# In[1]:


import pandas as pd
import altair as alt
movie_rev_actor = pd.read_csv('data/movie_rev_actor.csv')
movie_rev = pd.read_csv('data/movie_rev_cleaned.csv')
print(movie_rev.info())


# In[2]:


# switch Dtype to datetime
movie_rev['release_date'] = movie_rev['release_date'].astype('datetime64')
print(movie_rev.info())


# In[3]:


#import function
from scripts import its_the_final_function as ff


# Here is the code used the create the above function
# ## code block 1
# 
# ```python
# 
# def custom_count_mean(data, grouping_col, string_name, mean_col):
#     import pandas as pd
#     """
#     Given a dataframe, a column and string, return the count and mean of a specified string with said column
#     
#     Parameters
#     ----------
#     data : pandas.core.frame.DataFrame
#         The dataframe to sample from
#     string_name : str
#         The string you want to count and find mean of
#     mean_col : float
#         The column you want to find the mean and count of
#         
#     Returns
#     -------
#     
#         The mean value and count of a string contained within a column
#         
#     Raises
#     ------
#     TypeError
#         If the input argument data is not of type pandas.core.frame.DataFrame
#     AssertError
#         If the input argument grouping_col is not in the data columns
#     AssertError
#         If the input argument action_col is not in the data columns
#     TypeError
#         If the string_name does on apper in the grouping_col
#     
#     Examples
#     --------
#     >>> custom_count_mean(movie_rev, 'voice_actor', 'Kristen Bell', 'inflation_adjusted_gross' )
#     (1, 414997174.0)
# 
#     """
#     
#     # Checks if a dataframe is the type of object being passed into the data argument
#     if not type(data) == pd.DataFrame: 
#         raise TypeError("The data argument is not of type DataFrame")
#     
#     # Tests that the the grouping column is in the dataframe
#     assert grouping_col in data.columns, "The grouping column does not exist in the dataframe"
#     
#     # Tests that the the mean_col column is in the dataframe
#     assert mean_col in data.columns, "The mean column does not exist in the dataframe"
#     
#     #tests that the string_name in in the grouping_col
#     if not data[grouping_col].str.contains(string_name).any():
#         raise TypeError("The string_name does appear in grouping_col")
#     
#     # compute count
#     count = data.groupby(grouping_col)[mean_col].count().reset_index().set_index(grouping_col).loc[string_name,mean_col]
# 
#     # compute mean
#     mean = data.groupby(grouping_col)[mean_col].mean().reset_index().set_index(grouping_col).loc[string_name,mean_col]
#     
#     # return the result
#     return(count, mean)
# ```

# ## Equation 1
# 
# The above function uses mean:
# 
# $$
# {\bar{x} = {\frac {x_{1}+x_{2}+\cdots +x_{n}}{n}}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}
# $$
# 
# 

# ## code block 2
# Here is the code used to create the below function test
# 
# ```python
# import pandas as pd
# from its_the_final_function import custom_count_mean
# 
# def test_one():
#     raw = {'id': [1873, 4913, 4801, 4540, 3581,
#                    4534, 1934, 4944, 1983, 1266], 
#            'name': ['English Oak', 'Higan Cherry', 'Willow Oak', 
#                     'Yoshino Cherry', 'Red Oak', 'Kindred Spirit Oak',
#                     'Garry Oak', 'Accolade Cherry', 'Snow Goose Cherry',
#                     'Evergreen Oak'], 
#             'neighbourhood': ['Sunset','West end','Kitsilano', 'Sunset', 
#                               'Arbutus-ridge','Arbutus-ridge', 'Kitsilano', 
#                               'West end','Kitsilano', 'Arbutus-ridge'],
#             'type': ['Oak', 'Cherry', 'Oak', 'Cherry', 'Oak',
#                      'Oak', 'Oak', 'Cherry', 'Cherry', 'Oak'],
#             'diameter': [9.0, 27.0, 3.0, 22.0, 3.0,
#                          6.5, 12.0, 18.0, 8.5, 23.0]}
#     helper_data = pd.DataFrame.from_dict(raw)
#     
#     # Tests that the expected count and mean are returned
#     assert custom_count_mean(helper_data, 'neighbourhood', 'Sunset','diameter') == (2, 15.5)
#     return
# 
# def test_two():
#     raw = {'id': [1873, 4913, 4801, 4540, 3581,
#                    4534, 1934, 4944, 1983, 1266], 
#            'name': ['English Oak', 'Higan Cherry', 'Willow Oak', 
#                     'Yoshino Cherry', 'Red Oak', 'Kindred Spirit Oak',
#                     'Garry Oak', 'Accolade Cherry', 'Snow Goose Cherry',
#                     'Evergreen Oak'], 
#             'neighbourhood': ['Sunset','West end','Kitsilano', 'Sunset', 
#                               'Arbutus-ridge','Arbutus-ridge', 'Kitsilano', 
#                               'West end','Kitsilano', 'Arbutus-ridge'],
#             'type': ['Oak', 'Cherry', 'Oak', 'Cherry', 'Oak',
#                      'Oak', 'Oak', 'Cherry', 'Cherry', 'Oak'],
#             'diameter': [9.0, 27.0, 3.0, 22.0, 3.0,
#                          6.5, 12.0, 18.0, 8.5, 23.0]}
#     helper_data = pd.DataFrame.from_dict(raw)
#     
#     # Tests that the expected count and mean are returned
#     assert custom_count_mean(helper_data, 'type', 'Cherry','diameter') == (4, 18.875)
#     return
# ```
# 

# In[4]:


#test function

get_ipython().system('pytest scripts\\final_test.py')


# In[5]:


#how many disney movies has Kristen Bell appeared in and how much did they gross after inflation on average?
kristen_bell = ff.custom_count_mean(movie_rev_actor,'voice-actor', 'Kristen Bell', 'inflation_adjusted_gross')
kristen_bell


# ## Insert image 1
# 
# ```{figure} images/kristen-bell.png
# ---
# width: 25%
# name: Kristen Bell
# alt: Krissy B
# ---
# Image of Kristen Bell
# ```

# In[6]:


#now lets try John Goodman

john_goodman = ff.custom_count_mean(movie_rev_actor,'voice-actor', 'John Goodman', 'inflation_adjusted_gross')
john_goodman


# ## Insert image 2
# 
# ```{figure} images/john-goodman.png
# ---
# width: 50%
# name: John Goodman
# alt: Johny G
# ---
# Image of John Goodman
# ```

# To how average revenue by actor compares to the overall average we will need to calcucate the overall average movie revenue for movies released since 1999.

# In[7]:


movie_rev_1999 = movie_rev.loc[(movie_rev['release_date'] >= '1999-01-01')]
movie_rev_1999.sort_values(by='release_date', ascending=True).head()


# Above I test the function against some helper data to ensure it is returning the correct values

# In[8]:


#Find mean movie revenue of movie realeased after 1999-01-01

mean_rev_a1999  =movie_rev_1999['inflation_adjusted_gross'].mean()

mean_rev_a1999


# Above I test the function against some helper data to ensure it is returning the correct values

# In[9]:


movie_rev_1999_group = movie_rev_1999.groupby('genre')['inflation_adjusted_gross'].sum().sort_values(ascending=False)
movie_rev_1999_group.head()

movie_rev_1999_group = movie_rev_1999_group.reset_index()
movie_rev_1999_group.head()


# Here is are two more interesting charts we can use to visualize the data

# #### hidden content chart #1

# In[10]:


#plot by genre

genre_rev_plot = (
    alt.Chart(movie_rev_1999_group[:10], width=1000, height=300)
    .mark_bar()
    .encode(
        x=alt.X("genre:N",sort="-y", title="Genre"),
        y=alt.Y("inflation_adjusted_gross:Q", title="Movie Revenue by genre"),
    )
    .properties(title="Figure 1: Top 10 Movie Revenue inflation adjusted by genre since 1999")
)
genre_rev_plot


# #### hidden input chart #2
# Here is the same data in a pie chart

# In[11]:


genre_rev_pie = (
    alt.Chart(movie_rev_1999_group)
    .mark_arc()
    .encode(
        theta=alt.Theta("inflation_adjusted_gross:Q", title="Movie revenue by Genre"),
        color=alt.Color("genre:N", title="Genre"),
    )
    .properties(title="Figure 2: Movie Revenue inflation adjusted by genre since 1999")
)
genre_rev_pie


# ## possible future analysis
# 
# In the future project to could be useful to run a linear regression analysis of the data sets. This could help show us any correlation between different variables in the data. Below is one formula that might be helpful in that analysis:
# 
# ### Equation 2
# 
# Sample Regression line:
# 
# $$
# \begin{equation}
# \hat{Y}_i = \hat{\beta}_0 + \hat{\beta}_1 X_i + \hat{\epsilon}_i
# \end{equation}
# $$
# 
# Source: https://linareskevin.wordpress.com/2015/09/17/linear-regression-equation-in-latex-using-texmaths-under-libreoffice/
# 
