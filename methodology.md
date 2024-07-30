---
title: Methodology
feature_text: |
  ## Methodology

---

## Data: the LoBo Corpus

The LovelyBooks corpus (LoBo corpus) consists of approx. 1,4 mio. book reviews in 16 genres. The distribution (in absolute numbers) and the respective genres can be found in the following plot:

{% include figure.html image="/assets/images/total_reviews_per_genre_BAR.png" position="center" height="90%" %} 

Note: "NaN" is a genre category defined by LovelyBooks which means something like "Other Genres".

## Sub-Corpus Building

It was decided to focus on a single genre, due to two reasons:
1. to avoid possible biases by genre specifics (e.g. that some genre are known to be more positive than others);
2. to keep the number of reviews and thus, the computing power, manageable.

The aim consisted in building two sub-corpora (one with incentivized and one with non-incentivized reviews) of a singe genre. The genre selection was based on the number of available reviews as it was conceivable that the absolute number of incentivized reviews (IRs) would be much smaller than that of non-incentivized reviews (NIRs) (confirmed also by Hu et al. [2023]). Thus, the genre with the highest number of IRs was selected and the respective size worked as the benchmark for the sub-corpus of NIRs.

### Identification of IRs

To detect IRs, this study followed the approach by Hu et al. and Costa et al. who created lists of deterministic terms and phrases to detect IRs. The present work goes back to the observation that book reviewers explicitly mention their honest opinions although they have received a free review copy on LovelyBooks. Thus, the main assumption is that a book review is incentivized if such a non-monetary incentive is explicitly referenced in the review. 

The following table presents the results of close-reading randomly selected reviews which match a given list of possible disclosure terms:

{% include figure.html image="/assets/images/Disclosures_Summary.png" position="center" height="90%" %} 

### Identification of NIRs
To identify NIRs, this study assumes that a review which is not explicitly marked as being incentivized is non-incentivized. Although this harbors the risk that the NIR corpus contains false-negative reviews (reviews that are incentivized but don't contain an explicit reference), this approach seemed more promising than trying to targetedly identify NIRs, for example by searching for reviews that explicitly mention a purchase intention.

### Genre Selection
The following plot presents an overview over the shares of IRs per genre:

{% include figure.html image="/assets/images/reviews_IR_shares_ALL.png" position="center" height="90%" %} 

As can be seen, the IR shares range from 0,18% (for the classics genre) to 5,6% (for the erotic literature genre). Nevertheless, this thesis aimed at selecting the genre with the highest possible number of IRs. Thus, the absolute numbers as presented in the following plot are of higher relevance:

{% include figure.html image="/assets/images/reviews_IRs_absolute_per_genre_BAR.png" position="center" height="90%" %} 

As the romance genre has the highest number of IRs, it was selected for the analyses.

### Review Type Analysis
On LovelyBooks, different kinds of reviews can be published:
1. normal reviews ("Rezensionen")
2. short reviews up to 140 characters ("Kurzmeinungen")

While these types are easy to detect in the data (it is a "Kurzmeinung" in case the term marks the review's beginning), a combined form of review, where the Kurzmeinung precedes the actual review, were also found in the data.

Overall, there are three cases of review types:
1. Kurzmeinung
2. Kurzmeinung & Rezension
3. Rezension

The following plot shows the distribution of the review types in the romance genre:

{% include figure.html image="/assets/images/review_type_shares_romance.png" position="center" height="90%" %} 

As type 1-reviews are very short, they do not convey much meaning. Thus, it was decided to exclude them from the analysis.

### Summary
In a last step, non-German reviews were detected and excluded from the corpus. Overall, the reduced romance corpus contains 109 553 reviews, out of these 4872 IRs. Thus, 4872 NIRs were randomly selected and both sub-corpora saved separately. 


## Pre-Processing

## Analysis

