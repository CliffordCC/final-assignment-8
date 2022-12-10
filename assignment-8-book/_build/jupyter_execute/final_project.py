#!/usr/bin/env python
# coding: utf-8

# # Final Project

# # Exploratory data analysis of the Disney dataset

# Clifford Childs created December 20th 2021

# ## Forward
# 
# This notebook will be exploring `Disney` dataset. This document will answer some general questions about the dataset while also demonstating the Python compencies I have developed through the 8 modules of Python for Data Science.
# 
# 

# # Introduction
# 
# ## Question(s) of interests
# 
# In the analysis I will be investigating questions related to the revenue and disney films Disney datasets.I will be exploring information related to movie revenue by voice actor. I am primarily interested in looking films that were made after 1999 because I believe that data will me more relavent to the present day film industry. I believe that acotors who on average gross more revenue per film will appear in more films since disney will be more interested in casting them.
# 
# ## Dataset description 
# 
# The below descripitions were taken directly from the [website]() where the datasets were originally obtained.
# 
# "All Disney movies with their release dates, genre, rating, total gross and inflation adjusted gross(2016).
# Disney has produced many movies, this data has all Disney movies till 2016."
# 
# 
# The `Disney` dataset is composed of 5 tables `disney_movies_total_gross.csv`, `disney_revenue_1991-2016.csv`, `disney-characters.csv`, `disney-directors.csv`, `disney-voice-actors.csv`. Each table is stored as a `.csv` file. The data set contains the release dates, genre, rating, total gross and inflation adjust gross of all disney movies made to to 2016; disney reveunue by source from 1991 to 2016; disney's characters catagorized by charater type (villian or hero) and including columns for films starred in, films release dates and film theme song; a list of disney directors and the films they directed; and, a list of all disney voice actors and the films the appeared in.
# 

# # Methods and Results

# Since I am interested in revenue by film and revenue by voice actor, I will only need to import `disney_movies_total_gross.csv` and `disney-voice-actors.csv` tables.
# 
# I will start by my importing the relavent data frames some proform some visualizations to give me an overview of the types and data we will be working with and to identify and data wrangling that needs to be done.

# In[1]:


#import data libaries that will need for this project
import altair as alt
import pandas as pd

#import required datatables and parse date field
movie_rev = pd.read_csv('data/disney_movies_total_gross.csv',  parse_dates = ['release_date'])
actor = pd.read_csv('data/disney-voice-actors.csv')


# Here is what the tables look like:

# In[2]:


movie_rev.head()


# In[3]:


actor.head()


# To help us learn more about the datasets I will run some `.info` and `.shape` tests. This will help give me an idea of size of my data, the dtypes within my data and the cleanliness of my data

# First here is some more info on the `movie_rev` dataframe:

# In[4]:


movie_rev.shape


# In[5]:


movie_rev.info()


# And now here is some more information on `actor` dataframe:

# In[6]:


actor.shape


# In[7]:


actor.info()


# I can see right away that all of the Dtypes in my `movie_rev` dataframe arre listed as objects with expection of the `release_date` columnn that I imported using `parse date` above. They also have several Null values in the genre column. I will start by cleaning this dataframe so that it better suited to answer the questions I have asked above.

# In[8]:


#filling null values in the genre columns with 'unknown'
movie_rev = movie_rev.assign(genre = movie_rev['genre'].fillna('unknown'))
movie_rev.info()


# In[9]:


# remove $ and ,  from total_gross and total_gross and convert to float
movie_rev = movie_rev.assign(total_gross = movie_rev['total_gross'].str.replace('$','',regex = True).str.replace(',','',regex = True).astype(float))
movie_rev.head()


# In[10]:


# remove $ and ,  from total_gross and inflation_adjusted_gross and convert to float
movie_rev = movie_rev.assign(inflation_adjusted_gross = movie_rev['inflation_adjusted_gross'].str.replace('$','',regex = True).str.replace(',','',regex = True).astype(float))
print(movie_rev.info())


# Great! I have fixed the null values and converted the `gross_total` and `inflation_adjusted_gross` dtypes to`float`

# Many of the movies in the dataset do not list any box office revenue. It is reasonable to believe that these movies were not released in theaters. Here I am going to remove them.

# In[11]:


#emove all columns with 0 gross
movie_rev = movie_rev[movie_rev['total_gross'] != 0]
#check that all zero values have been eliminated
movie_rev.sort_values(by='total_gross', ascending=True).head()


# Now that the dataframes have been cleaned I will merge them together so that that we can work with them in one dataframe.

# In[12]:


#rename "movie_title" column to so the dataframes are consistent
movie_rev = movie_rev.rename(columns={'movie_title':'movie'})

#remove leading and trailing spaces from movie columns in mergerd dataframes

movie_rev.assign(movie = movie_rev['movie'].str.strip())
actor.assign(actor = actor['movie'].str.strip())


#merge using inner becuase we are only interested in movies with voice actors

movie_rev_actor = movie_rev.merge(actor,
                                  left_on='movie', 
                                  right_on='movie',
                                  how='inner')
movie_rev_actor = movie_rev_actor[movie_rev_actor['voice-actor'] != 'None']

movie_rev_actor.head()
## make sure all voice-actor with eligable movies are in the dataframe


# We now have a dataframe that can be used for analyzing revenue by voice actor. However our inquiry question above only cares about modern movies. Below I am going to filter movies that were released before January 1st 1999.
# 

# In[13]:


#remove all films that were releassed before 1999, to ensure the data is somewhat relative to modern day

movie_rev_actor = movie_rev_actor.loc[(movie_rev_actor['release_date'] >= '1999-01-01')]

movie_rev_actor.sort_values(by='release_date', ascending=True).head()


# Now lets take a look at average revenue by voice-actor.

# In[14]:


# group by voice actor and compute the average number of parts.

rev_actor_group = pd.DataFrame(movie_rev_actor.groupby('voice-actor')['inflation_adjusted_gross'].mean().sort_values(ascending=False))

#reset index so we can plot

rev_actor_group = rev_actor_group.reset_index()
rev_actor_group.head()


# Now lets plot out the top 20 actors by average revenue by movie.

# In[15]:


#plot top 20 highest averages using altiar

voice_actor_plot = (
    alt.Chart(rev_actor_group[:20], width=1000, height=300)
    .mark_bar()
    .encode(
        x=alt.X("voice-actor:N",sort="-y", title="Voice Actor"),
        y=alt.Y("inflation_adjusted_gross:Q", title="Average Movie Revenue"),
    )
    .properties(title="Figure 1: Top 20 Average Movie Revenue by Voice Actor inflation adjusted since 1999")
)
voice_actor_plot




# How many movies did each actor star in? 

# In[16]:


# group by year and compute the average number of parts.

count_actor_group = movie_rev_actor.groupby('voice-actor')['movie'].count().sort_values(ascending=False)
count_actor_group.head()

count_actor_group = count_actor_group.reset_index()
count_actor_group.head()


# In[17]:


#plot top 75 highest appearance in movies using altiar

count_actor_plot = (
    alt.Chart(count_actor_group[:20], width=1000, height=300)
    .mark_circle()
    .encode(
        x=alt.X("voice-actor:N",sort="-y", title="Voice Actor"),
        y=alt.Y("movie:Q", title="movie appearances"),
    )
    .properties(title="Figure 2: nummber of films by Voice Actor since 1999 (top 20 actors)")
)
count_actor_plot


# The above plost shows us the that there relatively few actors who have not more than one film since 1999. We can see that Kirsten Bell has the highest grossing average but has only starred in one movie.

# Now I will create a function the reads in a dataframe and returns the counts and average of a specific columns for a specific string. This will be a helpful tool to quickly see how many movies a given actor has been in and how much revenue they have grossed on average per moive. However, it can also be used to get other interesting stats such as revenue by genre and it can be reused on any dataframe that contains columns with strings and columns with floats.

# In[18]:


#import function
from scripts import its_the_final_function as ff


# In[19]:


#test function

get_ipython().system('pytest scripts\\final_test.py')


# In[20]:


#how many disney movies has Kristen Bell appeared in and how much did they gross after inflation on average?
kristen_bell = ff.custom_count_mean(movie_rev_actor,'voice-actor', 'Kristen Bell', 'inflation_adjusted_gross')
kristen_bell


# In[21]:


#now lets try John Goodman

john_goodman = ff.custom_count_mean(movie_rev_actor,'voice-actor', 'John Goodman', 'inflation_adjusted_gross')
john_goodman


# To see how average revenue by actor compares to the overall average we will need to calucate the overall average movie revenue for movies released since 1999.

# In[22]:


movie_rev_1999 = movie_rev.loc[(movie_rev['release_date'] >= '1999-01-01')]
movie_rev_1999.sort_values(by='release_date', ascending=True).head()


# Above I test the function against some helper data to ensure it is returning the correct values

# In[23]:


#Find mean movie revenue of movie realeased after 1999-01-01

mean_rev_a1999  =movie_rev_1999['inflation_adjusted_gross'].mean()

mean_rev_a1999


# Above we can see that Kristen Bell and John Goodman appear in one and two films respectively since 1999 but that the movies they were in grossed above the average movie released by disney since 1999.

# # Discussions

#  In the analysis I tried compute average revenue of movies starred in by each voice actor and the average number of movies they had starred in since 1999. First I imported the relavant datasets and then using `.info()` looked at how the data was being stored. I then cleaned and and merged the `disney_voice_actor` dataset with the `disney_movies_total_revenue` data set. I then performed several visualizations that helped me answer my intitial question. I also created a function that pulls the the number of movies and average revenue per movie for a specfic actor. This acts a search function of the data. I is usefull for looking up specfic information on a specfic actor.
#  
#  I was quite suprised by my results. Very few actors appeared in more that one movie since 1999. Further the actors who appeared in more films generally had a lower average movie revenue for the movies they starred in. I expected that disney would cast actors more often once they had a successfull movie but that does to appear to be what is happening. This could be becuase the genre and theme of the movie matter more than the actors who starred in them.
#  
#  One interesting question to explore on this data could be to see if there is a correlation between average revenue by genre and number of movies created under that specific genre. It would be very interesting to compare the results of that analysis to my results. It could also be interesting to expand that analysis beyond just disney movies if those datasets exist. This would interesting becuase it would allow disney to begin focus that production budgets on genres and actors that on avergae earn the studio more revenue.
#  

# # References
# 
# Not all the work in this notebook is original. Some of the code was taken from various online sources including https://stackoverflow.com/, the various Modules and assigments in 'Python for Data Science' and the 'Sample Project'. I take no credit for parts that are not mine.
# 
# 
# ## Resources used
# 
# Data Souce:
# 
#     `disney data set` provided through Python for Data Science
# 
# Trouble shooting:
# 
#     https://stackoverflow.com/  and modules 1 through 8 in Python for Data Science were used to trouble shoot the many errors I came accross.
#     
