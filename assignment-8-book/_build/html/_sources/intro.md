# Introduction

## Question(s) of interests

In the analysis I will be investigating questions related to the revenue and disney films Disney datasets.I will be exploring information related to movie revenue by voice actor. I am primarily interested in looking films that were made after 1999 because I believe that data will me more relavent to the present day film industry. I believe that acotors who on average gross more revenue per film will appear in more films since disney will be more interested in casting them.

## Dataset description 

The below descripitions were taken directly from the [website](https://www.kaggle.com/prateekmaj21/disney-movies) where the datasets were originally obtained.

"All Disney movies with their release dates, genre, rating, total gross and inflation adjusted gross(2016).
Disney has produced many movies, this data has all Disney movies till 2016."


The `Disney` dataset is composed of 5 tables `disney_movies_total_gross.csv`, `disney_revenue_1991-2016.csv`, `disney-characters.csv`, `disney-directors.csv`, `disney-voice-actors.csv`. Each table is stored as a `.csv` file. The data set contains the release dates, genre, rating, total gross and inflation adjust gross of all disney movies made to to 2016; disney reveunue by source from 1991 to 2016; disney's characters catagorized by charater type (villian or hero) and including columns for films starred in, films release dates and film theme song; a list of disney directors and the films they directed; and, a list of all disney voice actors and the films the appeared in.

## Math literacy requirement.

To effectively understand this project the reader should have and understanding very basics statistical equations such as:

### Mean:

$$
{\bar{x} = {\frac {x_{1}+x_{2}+\cdots +x_{n}}{n}}}={\frac {1}{n}}\sum _{i=1}^{n}x_{i}
$$

### Median:

$$
{Med{(X)} = \frac{X[\frac {n}{2}]+X[\frac{n}{2}+1]}{2}{\text{if n is even}}}
$$
Where X = ordered list

### Standard Deviation:

$$
\sigma = \sqrt{\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2}
$$
```{margin} Did you know?
Did you know the Karl Pearson introduced procedure and term standard deviation to statistics in 1892.
```

###  Variance:

$$
\sigma ^2 = {\frac{1}{N-1} \sum_{i=1}^N (x_i - \overline{x})^2}
$$

```{tip} 
Std dev is just the square root of the variance [https://www.encyclopedia.com/science-and-technology/mathematics/mathematics/standard-deviation]
```

## Python literacy requirement:

To get the most out of this project the reader should be able to read basic python code. Their are several code cells in the project that can be run live and manipulated direct within the jupyter book. Here are 2 examples of one code cell you will come across this book:

### code block example 1
```python
# group by year and compute the average number of parts.

count_actor_group = movie_rev_actor.groupby('voice-actor')['movie'].count().sort_values(ascending=False)
count_actor_group.head()

count_actor_group = count_actor_group.reset_index()
count_actor_group.head()
```
### code block example 2

```python
# group by year and compute the average number of parts.

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
```

```{note} 
Python was the second most used programming laungauge in 2022 [https://octoverse.github.com/2022/top-programming-languages]

```


```{tableofcontents}
```
