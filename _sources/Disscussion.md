# Discussions

In the analysis I tried compute average revenue of movies starred in by each voice actor and the average number of movies they had starred in since 1999. First I imported the relevant datasets and then using `.info()` looked at how the data was being stored. I then cleaned and and merged the `disney_voice_actor` dataset with the `disney_movies_total_revenue` data set. I then performed several visualizations that helped me answer my initial question. I also created a function that pulls the the number of movies and average revenue per movie for a specific actor. This acts a search function of the data. I is useful for looking up specific information on a specific actor.
 
 ```{figure} images/data-image.png
---
width: 50%
name: data image
alt: data
---
Image of data science
```
 
 I was quite suprised by my results. Very few actors appeared in more that one movie since 1999. Further the actors who appeared in more films generally had a lower average movie revenue for the movies they starred in. I expected that disney would cast actors more often once they had a successful movie but that does to appear to be what is happening. This could be because the genre and theme of the movie matter more than the actors who starred in them.
 
  
 ```{figure} images/results.png
---
width: 30%
name: results
alt: data
---
results image
```
 
 One interesting question to explore on this data could be to see if there is a correlation between average revenue by genre and number of movies created under that specific genre. It would be very interesting to compare the results of that analysis to my results. It could also be interesting to expand that analysis beyond just disney movies if those datasets exist. This would interesting because it would allow disney to begin focus that production budgets on genres and actors that on average earn the studio more revenue.
 
 ```{margin} Did you know?
This was my first ever data science project!
```
```{important}
My analysis in the book is only the beginning of what is possible with the powers of data science! Many more insights are left to be made.
```
```{tip}
Learning data science is hard but the most important tip I have received to to practice!
```
```{admonition} More useful statisical equations:
$$
\text{Sample Slope:}
\begin{equation}
\hat{\beta}_1 = \frac{\sum(X_i – \bar{X}) (Y_i – \bar{Y})} {\sum(X_i – \bar{X})^2}
\end{equation}
$$
+++
$$
\text{Conditional Standard Deviation:}
\begin{equation}
\hat{\sigma} = \sqrt\frac{\sum(Y_i – \hat{Y}_i)^2} {n – 2}
\end{equation}
$$
(Linares, 2015)
```
## Cross referencing
Here are links to some of important the figures and equations used in this notebook

{numref}`question mark`
{numref}`Kristen Bell`
{numref}`John Goodman`
{numref}`data image`
{numref}`results`
{eq}`mean`
{eq}`odd median`
{eq}`even median`
{eq}`Std Dev`
{eq}`Var`

# References

Not all the work in this notebook is original. Some of the code was taken from various online sources including https://stackoverflow.com/, the various Modules and assigments in 'Python for Data Science' and the 'Sample Project'. I take no credit for parts that are not mine.

A list of references can be found the reference.bib file in the public github repo linked at the top of this book

## Resources used

Data Souce:

    `disney data set` provided through Python for Data Science

Trouble shooting:

    https://stackoverflow.com/  and modules 1 through 8 in Python for Data Science were used to trouble shoot the many errors I came accross.
    