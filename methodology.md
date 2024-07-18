---
title: Methodology
feature_text: |
  ## Methodology

---

## Data: the LoBo Corpus

The LovelyBooks corpus (LoBo corpus) consists of approx. 1.4 mio. book reviews in 16 genres. The distribution (in absolute numbers) and the respective genres can be found in the following plot:

{% include figure.html image="/assets/images/total_reviews_per_genre_BAR.png" position="center" height="90%" %} 

Note: "NaN" is a genre category defined by LovelyBooks which means something like "Other Genres".

## Sub-Corpus Building

It was decided to focus on a single genre, due to two reasons:
1. to avoid possible biases by genre specifics (e.g. that some genre are known to be more positive than others);
2. to keep the number of reviews and thus, the computing power, manageable.

The aim consists in building two sub-corpora (one with incentivized and one with non-incentivized reviews) of a singe genre. The genre selection was based on the number of available reviews. It is conceivable that the absolute number of incentivized reviews (IRs) is much smaller than that of non-incentivized reviews (NIRs) (confirmed also by Hu et al. [2023]). Thus, the genre with the highest number of IRs was selected and the respective size works as the benchmark for the sub-corpus of NIRs.

### Identification of IRs

To detect IRs, this study follows the approach by Hu et al. and Costa et al. who create lists of deterministic terms
and phrases to detect IRs. The present work goes back to the
observation that book reviewers explicitly mention their honest opinions although they have received a free review copy on LovelyBooks. Thus, the main assumption is that a book review is incentivized if such a non-monetary incentive is explicitly referenced in the review. 

The following table presents the results of close-reading randomly selected reviews which match a given list of possible disclosure terms:

{% include figure.html image="/assets/images/Disclosures_Summary.png" position="center" height="90%" %} 



## Pre-Processing

## Analysis

