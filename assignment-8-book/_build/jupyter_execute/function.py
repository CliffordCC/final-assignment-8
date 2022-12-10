#!/usr/bin/env python
# coding: utf-8

# # Function

# In[1]:


#import function
from scripts import its_the_final_function as ff


# In[2]:


#test function

get_ipython().system('pytest scripts\\final_test.py')


# In[3]:


#how many disney movies has Kristen Bell appeared in and how much did they gross after inflation on average?
kristen_bell = ff.custom_count_mean(movie_rev_actor,'voice-actor', 'Kristen Bell', 'inflation_adjusted_gross')
kristen_bell


# In[ ]:


#now lets try John Goodman

john_goodman = ff.custom_count_mean(movie_rev_actor,'voice-actor', 'John Goodman', 'inflation_adjusted_gross')
john_goodman


# To how average revenue by actor compares to the overall average we will need to calcucate the overall average movie revenue for movies released since 1999.

# In[ ]:


movie_rev_1999 = movie_rev.loc[(movie_rev['release_date'] >= '1999-01-01')]
movie_rev_1999.sort_values(by='release_date', ascending=True).head()


# Above I test the function against some helper data to ensure it is returning the correct values

# In[ ]:


#Find mean movie revenue of movie realeased after 1999-01-01

mean_rev_a1999  =movie_rev_1999['inflation_adjusted_gross'].mean()

mean_rev_a1999


# Above I test the function against some helper data to ensure it is returning the correct values

# In[ ]:




