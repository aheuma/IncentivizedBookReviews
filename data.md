---
title: Data
layout: page

---

## The LoBo Corpus {#data-lobo-corpus}

The LovelyBooks corpus (LoBo corpus) is a dataset of German online book reviews which were collected by S. Rebora, B. Herrmann, and T. Messerli[^1]. The dataset comprises about 1.4 mio. book reviews, sorted by 16 genres. The distribution (in absolute numbers) and the respective genres can be found in the following plot:

{% include figure.html image="../assets/images/total_reviews_per_genre_BAR.png" position="center" height="90%" %} 

Note: "NaN" is a genre category defined by LovelyBooks which means something like "Other Genres".

In addition to the 16 genre files, there is a large metadata file which consists of 33 columns. The metadata file offers e.g. information on the book that the review is about, for example: the book’s title, author, or ISBN etc. Review-related information is also included, such as the star rating of the individual review or temporal information. Importantly, the reviews can always be matched by their unique ids.

Lastly, the following table presents an overview over the dataset:

| **Metric** | **Amount** |
| --- | --- |
| # of Reviews | 1,327,457 |
| # of Genres | 16 |
| # of Reviewers | 54,037 |
| # of Books | 169,759 |
| Most Reviews per Book | 1243 |
| Most Reviews per Reviewer | 55,033 |

---
[^1]: Rebora et al. 2022.