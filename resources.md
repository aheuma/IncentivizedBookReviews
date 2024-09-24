---
title: Resources
layout: page
pdf_file: "../assets/Hypothesenkapitel.pdf"
aside: true
---

Note that some files can not be published due to copyright restrictions. This applies for example to the master thesis or the tables that were used to check the accuracy of the IR and NIR detection approaches.

## Poster {#poster}

<object data="../assets/Resources/Other/MA_Poster.pdf" width="744" height="800" type='application/pdf'></object>

## Scripts {#scripts}

| Purpose |  |
| --- | --- |
| Transform token level data to review level | [File](../Resources/Scripts/createReviewLevelCSV_allGenres.py) | 
| Get review metadata | [File](../Resources/Scripts/getMetadata.py) | 
| Add incentivization status and review type to all reviews in all genres | [File](../Resources/Scripts/addColumns_allGenres.py) | 
| Create tables with 5 reviews per genre with potential disclosure terms |  [File](../Resources/Scripts/detectIRs.py) | 
| Create an overview table with (non-)incentivized reviews per genre | [File](../Resources/Scripts/summarizeIncentivizationStatus_allGenres.py) | 
| Create table with 5 reviews per genre with purchase intention | [File](../Resources/Scripts/detectNIRs_approach1DepMatch.py) | 
| Create table with 5 reviews per genre with incentivization status = 0 | [File](../Resources/Scripts/detectNIRs_approach2.py) | 
| Add additional column to romance reviews, indicating review language | [File](../Resources/Scripts/addColumn_Language_romance.py) |
| Create the two sub-corpora of IRs and NIRs |  [File](../Resources/Scripts/filterData_romance.py) | 
| Preprocess data | [File](../Resources/Scripts/preprocessData.py) | 
| Analyze H1: Positivity |  [File](../Resources/Scripts/analyzeH1Positivity.py) |
| Analyze H2: Complexity | [File](../Resources/Scripts/analyzeH2Complexity.py) |
| Analyze H3: Elaborateness |  [File](../Resources/Scripts/analyzeH3Elaborateness.py) |
| Analyze H4: Extremeness |  [File](../Resources/Scripts/analyzeH4Extremeness.py) |
| Analyze H5: Objectivity |  [File](../Resources/Scripts/analyzeH5Objectivity.py) |
| Test hypotheses H1-H3 and H5 |  [File](../Resources/Scripts/testHypotheses.py) |
| Test hypothesis H4 |  [File](../Resources/Scripts/testH4Extremeness.py) |
| Merge IR and NIR file for H4 | [File](../Resources/Scripts/mergeIRandNIR.py) |
| Create table with descriptive statistics for all analyses | [File](../Resources/Scripts/createDescriptiveOverview_romance.py) |
| Generate plots to visualize results |  [File](../Resources/Scripts/createPlots.py) |

<br>
## Generated Data {#generated-data}

| Purpose |   |
| --- | --- |
| Overview over shares of incentivized reviews per genre | [File](../Resources/Other/genre_overview_incentivization.xlsx) | 
| Comparison of incentivization shares with Hu et al. 2023 | [File](../Resources/Other/incentivization_comparison_Hu.xlsx) | 
| Summary of the accuracy of potential terms to detect incentivized reviews |  [File](../Resources/Other/IR_detection_summary.xlsx) | 
| Overview over the descriptive statistics for the five analyses | [File](../Resources/Other/descriptiveOverview_romance.csv) | 

<br>
## Plots {#plots}

| Content |  |
| --- | --- |
| Total number of reviews per Genre in the LoBo Corpus | [File](../Resources/Plots/total_reviews_per_genre_BAR.png) | 
| Share of incentivized reviews per genre |  [File](../Resources/Plots/reviews_IR_shares_ALL.png) | 
| Comparison of shares of incentivized reviews for different genres and sources |  [File](../Resources/Plots/hu_IR_comparison.png) |
| Absolute numbers of incentivized reviews per genre |  [File](../Resources/Plots/reviews_IRs_absolute_per_genre_BAR.png) | 
| Share of the review types in the romance genre |  [File](../Resources/Plots/review_type_shares_romance.png) |
| Distribution plot for H1 | [File](../Resources/Plots/H1_Distribution_AAP.png) |
| Distribution plot for H2 | [File](../Resources/Plots/H2_Distribution_AverageWordLength.png) |
| Distribution plot for H3 |  [File](../Resources/Plots/H3_Distribution_AverageReviewLength.png) |
| Distribution plot for H4 |  [File](../Resources/Plots/H4_Distribution_StarRatings.png) |
| Distribution plot for H5 |  [File](../Resources/Plots/H5_Distribution_ShareEmotionalWords.png) |

<br>
## Bibliography {#bibliography}

Börsenverein d. Deutschen Buchhandels, Abt. Marktforsch. u. Statistik (Ed.). (2024). _Buch und Buchhandel in Zahlen 2024_: Zahlen, Fakten und Analysen zur wirtschaftlichen Entwicklung. MVB.

Costa, A., Guerreiro, J., Moro, S., & Henriques, R. (2019). Unfolding the characteristics of incentivized online reviews. _Journal of Retailing and Consumer Services_, 47, 272–281. [DOI](https://doi.org/10.1016/j.jretconser.2018.12.006).

Friestad, M., & Wright, P. (1994). The Persuasion Knowledge Model: How People Cope with Persuasion Attempts. _Journal of Consumer Research_, 21(1), 1–31. [DOI](https://doi.org/10.1086/209380).

Gouldner, A. W. (1960). The Norm of Reciprocity: A Preliminary Statement. _American Sociological Review_, 25(2), 161. [DOI](https://doi.org/10.2307/2092623).

Heider, F. (1958). The psychology of interpersonal relations (pp. ix, 326). John Wiley & Sons Inc. [DOI](https://doi.org/10.1037/10628-000).

Hu, Y., LeBlanc, Z., Diesner, J., Underwood, T., Layne-Worthey, G., & Downie, J. S. (2023). Complexities of leveraging user-generated book reviews for scholarly research: Transiency, power dynamics, and cultural dependency. _International Journal on Digital Libraries_. [DOI](https://doi.org/10.1007/s00799-023-00376-z).

Incentivization. (2024). _Collins Dictionary_. Harper Collins. [URL](https://www.collinsdictionary.com/de/worterbuch/englisch/).

Kim, S. J., Maslowska, E., & Tamaddoni, A. (2019). The paradox of (dis)trust in sponsorship disclosure: The characteristics and effects of sponsored online consumer reviews. _Decision Support Systems_, 116, 114–124. [DOI](https://doi.org/10.1016/j.dss.2018.10.014).

Landesmedienanstalten. (2019, January 23). Leitfaden der Medienanstalten – Werbekennzeichnung bei Online-Medien 2018. die medienanstalten – ALM GbR. [URL](https://web.archive.org/web/20190123123317/https://www.die-medienanstalten.de/fileadmin/user_upload/Rechtsgrundlagen/Richtlinien_Leitfaeden/Leitfaden_Medienanstalten_Werbekennzeichnung_Social_Media.pdf).

Lauer, G. (2020). Lesen im digitalen Zeitalter. wbg Academic.

Li, Y., & Zhang, L. (2021). Do online reviews truly matter? A study of the characteristics of consumers involved in different online review scenarios. _Behaviour & Information Technology_, 40(13), 1448–1466. [DOI](https://doi.org/10.1080/0144929X.2020.1759691).

LovelyBooks. (2024, January). Mediadaten für Verlage. [URL](https://s3-eu-west-1.amazonaws.com/media.lovelybooks.de/LovelyBooks-Mediadaten-Verlage-24-01.pdf).

Pleimling, D. (2012, February 10). Social Reading—Leben im digitalen Zeitalter. _Aus Politik und Zeitgeschichte_. [URL](https://www.bpb.de/shop/zeitschriften/apuz/145378/social-reading-lesen-im-digitalen-zeitalter/).

Rebora, S., Messerli, T., & Herrmann, J. B. (2022, March 7). Towards a Computational Study of German Book Reviews—A Comparison between Emotion Dictionaries and Transfer Learning in Sentiment Analysis. _DHd2022: Kulturen des digitalen Gedächtnisses_. [DOI](https://doi.org/10.5281/ZENODO.6328141).

Stein, S. (2015). Laienliteraturkritik—Charakteristika und Funktionen von Laienrezensionen im Literaturbetrieb. In H. Kaulen & C. Gansel (Eds.), _Literaturkritik heute: Tendenzen—Traditionen—Vermittlung_ (pp. 59–76). V&R unipress.
