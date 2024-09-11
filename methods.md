---
title: Methods
aside: true
layout: page

---

## The LoBo Corpus {#data-lobo-corpus}

The LovelyBooks corpus (LoBo corpus) is a dataset of German online book reviews which were collected by S. Rebora, B. Herrmann, and T. Messerli[^1]. The dataset comprises about 1,4 mio. book reviews, sorted by 16 genres. The distribution (in absolute numbers) and the respective genres can be found in the following plot:

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

## Sub-Corpus Building {#sub-corpus-building}

It was decided to focus on a single genre, due to two reasons:
1. to avoid possible biases by genre specifics (e.g. that some genre are known to be more positive than others);
2. to keep the number of reviews and thus, the computing power, manageable.

The aim consisted in building two sub-corpora (one with incentivized and one with non-incentivized reviews) of a singe genre. The genre selection was based on the number of available reviews as it was conceivable that the absolute number of incentivized reviews (IRs) would be much smaller than that of non-incentivized reviews (NIRs)[^2]. Thus, the genre with the highest number of IRs was selected and the respective size worked as the benchmark for the sub-corpus of NIRs.

#### Identification of IRs {#identification-irs}

To detect IRs, this study followed the approach by two other studies[^3] who created lists of deterministic terms and phrases to detect IRs. The present work goes back to the observation that book reviewers explicitly mention their honest opinions although they have received a free review copy on LovelyBooks. Thus, the main assumption is that a book review is incentivized if such a non-monetary incentive is explicitly referenced in the review. 

The following table presents the results of close-reading randomly selected reviews which match a given list of possible disclosure terms:

{% include figure.html image="../assets/images/Disclosures_Summary.png" position="center" height="90%" %} 

#### Identification of NIRs {#identification-nirs}
To identify NIRs, this study assumes that a review which is not explicitly marked as being incentivized is non-incentivized. Although this harbors the risk that the NIR corpus contains false-negative reviews (reviews that are incentivized but do not contain an explicit reference), this approach prooved to be more accurate than another approach, for example by searching for reviews that explicitly mention a purchase intention.

#### Genre Selection {#genre-selection}
The following plot presents an overview over the shares of IRs per genre:

{% include figure.html image="../assets/images/reviews_IR_shares_ALL.png" position="center" height="90%" %}

As can be seen, the IR shares range from 0.18% (for the classics genre) to 5.6% (for the erotic literature genre). Nevertheless, this thesis aimed at selecting the genre with the highest possible number of IRs. Thus, the absolute numbers as presented in the following plot are of higher relevance:

{% include figure.html image="../assets/images/reviews_IRs_absolute_per_genre_BAR.png" position="center" height="90%" %} 

As the romance genre has the highest number of IRs, it was selected for the analyses.

#### Review Type Analysis {#review-type-analysis}
On LovelyBooks, different kinds of reviews can be published:
1. normal reviews ("Rezensionen")
2. short reviews up to 140 characters ("Kurzmeinungen")

While these types are easy to detect in the data (it is a "Kurzmeinung" in case the term marks the review's beginning), a combined form of review, where the Kurzmeinung precedes the actual review, were also found in the data.

Overall, there are three cases of review types:
1. Kurzmeinung
2. Kurzmeinung & Rezension
3. Rezension

The following plot shows the distribution of the review types in the romance genre:

{% include figure.html image="../assets/images/review_type_shares_romance.png" position="center" height="90%" %} 

As type 1-reviews are very short, they do not convey much meaning. Thus, it was decided to exclude them from the analysis.

#### Interim Summary {#interim-summary}
In a last step, non-German reviews were detected and excluded from the corpus. Overall, the reduced romance corpus contains 109,553 reviews, out of these 4,872 IRs. Thus, 4,872 NIRs were randomly selected and both sub-corpora saved separately. 


## Pre-Processing {#pre-processing}
With consideration of the hypotheses specifications, an approach was chosen which modifies the raw data as less as possible. Overall, the following steps have been carried out:

1. Unification of quotation marks;
2. Deletion of emoticons and special characters;
3. Deletion of review type indicator.

Quotation marks were unified to avoid potential parsing issues. Emoticons and special characters were deleted because they were found to distort Parts-of-Speech-tagging accuracy. And lastly, the review type indicator ("Kurzmeinung") which was most probably inserted automatically by the platform was deleted.

#### Handling Disclosure Statements {#handling-disclosure-statements}

Kim et al. do not include the disclosure phrase in their analyses because, e.g. for the hypothesis about review elaborateness, this additional sentence could distort the results.

The present thesis follows a different approach. This is mainly due to the function that the disclaimer serves. In Kim et al.’s study, the only purpose of the disclaimer is to inform readers that the reviewer has been sponsored. It does not include e.g. a product-related statement. Thus, it has no relevance for the actual analysis. For the disclaimers in the LoBo corpus, the case is different. Here, the disclaimers serve a dual function: While they are used to identify sponsored reviews, there are also cases where this disclaimer is part of an evaluative statement about the book or the reading experience. Therefore, it can be argued that the sentences expressing gratitude for having received a free book—the disclaimers—contain product-related evaluations by book reviewers. Thus, the disclaimers are not removed for any of the hypotheses.

## Formalization & Operationalization {#formalization-operationalization}
The following table shows an overview over the approach used by this study to formalize and operationalize the hypotheses. The asterisk character (*) marks parts were this thesis uses a different approach compared to Kim et al.

| | Hypothesis | Formalization | Operationalization |
|---|---|---|---|
| H1 | IRs are more positive | Valence | SentiArt* |
| H2 | IRs are more complex | Ø Word length* | Character count per word* |
| H3 | IRs are more elaborate | Review length | Word count per review |
| H4 | IRs are less extreme | Star ratings | Compare star distribution |
| H5 | IRs are more objective | Share of emotional words* | LIWC-22 analysis* |

<br>
For all hypotheses, the values are computed and added to each review in a separate column. The following code snippet exemplifies this procedure for _H1_:



    def addAverageWordLengthToReview(input_path):
        input_df = pd.read_csv(input_path, sep=” ,”, header=0)
        input_df[ ’average word length ’ ] = ’ ’
        for index, row in input_df.iterrows():
            doc = nlp(row[ ’review content ’ ], disable=[”ner”])
            list_non_word_POS_tags = [”PUNCT”, ”NUM”, ”SYM”, ”X”, ”EOL”, ”SPACE”]
            word_lengths_per_review = []
            for token in doc:
                if token.pos_ not in list_non_word_POS_tags:
                    word_lengths_per_review.append(len(token.text))
            average_word_length = round(statistics.mean(word_lengths_per_review), 4)
            input_df.loc[index, ’average word length ’ ] = average_word_length
        input_df.to_csv(input_path, index=False, header=True)

---
[^1]: Rebora et al. 2022.
[^2]: Confirmed also by Hu et al. 2023.
[^3]: Costa et al. 2019, Hu et al. 2023.