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
# ## Insert Image 1
# 
# ![Disney logo image](https://cdn.mos.cms.futurecdn.net/qfFFFhnM8LwZnjpTECN3oB-1920-80.jpg.webp)
# 
# 

# # Methods and Results

# Since I am interested in revenue by film and revenue by voice actor, I will only need to import `disney_movies_total_gross.csv` and `disney-voice-actors.csv` tables.
# 
# I will start by my importing the relavent data frames some proform some visualizations to give me an overview of the types and data we will be working with and to identify and data wrangling that needs to be done.
# 
# ## Insert image 2
# 
# ```{figure} images/question_mark.png
# ---
# width: 50%
# name: question mark
# alt: question mark
# ---
# question mark image
# ```
# 

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


# saving cleaned dataframe so I can reference in another notebook

# In[12]:


movie_rev.to_csv('data/movie_rev_cleaned.csv')


# Now that the dataframes have been cleaned I will merge them together so that that we can work with them in one dataframe.

# In[13]:


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


# Saving new data frame as csv so it can be referenced in other files

# In[14]:


movie_rev_actor.to_csv('data/movie_rev_actor.csv')


# We now have a dataframe that can be used for analyzing revenue by voice actor. However our inquiry question above only cares about modern movies. Below I am going to filter movies that were released before January 1st 1999.
# 

# In[15]:


#remove all films that were releassed before 1999, to ensure the data is somewhat relative to modern day

movie_rev_actor = movie_rev_actor.loc[(movie_rev_actor['release_date'] >= '1999-01-01')]

movie_rev_actor.sort_values(by='release_date', ascending=True).head()


# Now lets take a look at average revenue by voice-actor.

# ## Markdown with block math equations 1
# 
# ### This is equation used to calculate mean below
# 
# ```{math}
# :label: mean
# {\bar{x} = {\frac {x_{1}+x_{2}+\cdots +x_{n}}{n}}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}
# ```
# 

# ## Markdown with block math equations 2
# 
# Although not used below know the Median could also be useful. This is the equation used to calculate median:
# 
# ```{math}
# :label: odd median
# {Med{(X)} = X\Bigg[\frac {n+1}{2}\Bigg]\text{if n is odd}}
# ```
# ```{math}
# :label: even median
# {Med{(X)} = \frac{X[\frac {n}{2}]+X[\frac{n}{2}+1]}{2}{\text{if n is even}}}
# +++
# \text{Where X=ordered list}
# ```
# 
# 
# 

# In[16]:


# group by voice actor and compute the average number of parts.

rev_actor_group = pd.DataFrame(movie_rev_actor.groupby('voice-actor')['inflation_adjusted_gross'].mean().sort_values(ascending=False))

#reset index so we can plot

rev_actor_group = rev_actor_group.reset_index()
rev_actor_group.head()


# Now lets plot out the top 20 actors by average revenue by movie.

# # Hidden input graph 1

# In[17]:


#plot top 20 highest averages using altiar. input hidden

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




# # block code 1
# Below is the code used to generate the above graph:
# 
# ```python
# #plot top 20 highest averages using altiar. input hidden
# 
# voice_actor_plot = (
#     alt.Chart(rev_actor_group[:20], width=1000, height=300)
#     .mark_bar()
#     .encode(
#         x=alt.X("voice-actor:N",sort="-y", title="Voice Actor"),
#         y=alt.Y("inflation_adjusted_gross:Q", title="Average Movie Revenue"),
#     )
#     .properties(title="Figure 1: Top 20 Average Movie Revenue by Voice Actor inflation adjusted since 1999")
# )
# voice_actor_plot
# ```
# 

# How many movies did each actor star in? 

# In[18]:


# group by year and compute the average number of parts.

count_actor_group = movie_rev_actor.groupby('voice-actor')['movie'].count().sort_values(ascending=False)
count_actor_group.head()

count_actor_group = count_actor_group.reset_index()
count_actor_group.head()


# # Hidden input graph 2

# In[19]:


#plot top 75 highest appearance in movies using altiar input hidden

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


# ## Code block 2
# 
# Below is the code used to generate the above graph
# 
# ```python
# count_actor_plot = (
#     alt.Chart(count_actor_group[:20], width=1000, height=300)
#     .mark_circle()
#     .encode(
#         x=alt.X("voice-actor:N",sort="-y", title="Voice Actor"),
#         y=alt.Y("movie:Q", title="movie appearances"),
#     )
#     .properties(title="Figure 2: nummber of films by Voice Actor since 1999 (top 20 actors)")
# )
# count_actor_plot
# ```
# 

# The above plot shows us the that there relatively few actors who have not more than one film since 1999. We can see that Kirsten Bell has the highest grossing average but has only starred in one movie.

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
