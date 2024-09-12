import pandas as pd
import scipy.stats as stats
from scipy.stats import shapiro
import seaborn as sns
import matplotlib.pyplot as plt
from statistics import quantiles

def createHistogramWithKDE(list_IR, list_NIR, xlabel, ylabel, plot_path):
    sns.histplot(data=list_IR, bins=20, color='blue', alpha=0.5, kde=True, label='IR')
    sns.histplot(data=list_NIR, bins=20, color='orange', alpha=0.5, kde=True, label='NIR')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.savefig(plot_path, dpi=300, bbox_inches='tight')
    
def checkNormality(list_IR, list_NIR):
    statistic_IR, pvalue_IR = shapiro(list_IR)
    statistic_NIR, pvalue_NIR = shapiro(list_NIR)
    print(f"IR: statistic-value: {round(statistic_IR, 4)}, p-value: {round(pvalue_IR, 4)}")
    print(f"NIR: statistic-value: {round(statistic_NIR, 4)}, p-value: {round(pvalue_NIR, 4)}")
    if pvalue_IR > 0.05:
        print("Normal distribution for IRs!")
    else:
        print("No normal distribution for IRs!")
    if pvalue_NIR > 0.05:
        print("Normal distribution for NIRs!")
    else:
        print("No normal distribution for NIRs!")  

def checkVariance(list_IR, list_NIR):
    levene_test = stats.levene(list_IR, list_NIR)
    if levene_test.pvalue > 0.05:
        print("Equality of variances is given!")
    else:
        print("No equality of variances!")
    print(round(levene_test.statistic, 4), round(levene_test.pvalue, 4))

def calculateMannWhitneyUtest(list_IR, list_NIR, hypothesis_type, label_hypothesis_test):
    mwu_results = stats.mannwhitneyu(list_IR, list_NIR, alternative=hypothesis_type)
    p_val = mwu_results.pvalue
    u_val = mwu_results.statistic
    print(f"Results for Hypothesis: {label_hypothesis_test}")
    print(f"U-Value: {round(u_val, 4)}")
    print(f"p-Value: {round(p_val, 4)}")
    if p_val < 0.05:
        print(f"Difference is significant.")
    else:
        print(f"Difference is not significant.")

def getQuantiles(list, sample_label):
    print(f"Quantiles for group: {sample_label}")
    print(f"{[round(q, 2) for q in quantiles(list, n=4)]}")

input_df_IR = pd.read_csv("./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv", sep=",", header=0)
input_df_NIR = pd.read_csv("./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv", sep=",", header=0)

# Test H1
AAP_IRs = input_df_IR['sentiment_aap']
AAP_NIRs = input_df_NIR['sentiment_aap']
createHistogramWithKDE(AAP_IRs, AAP_NIRs, "Ø AAP Score", "# of Reviews", "./Arbeitspakete/AP2_Analyse/Plots/Analysis/H1_Distribution_AAP.png")
checkVariance(AAP_IRs, AAP_NIRs)
calculateMannWhitneyUtest(AAP_IRs, AAP_NIRs, "less", "1: AAP")
getQuantiles(AAP_IRs, "IR")
getQuantiles(AAP_NIRs, "NIR")

# Test H2
averageWordLength_IRs = input_df_IR['average word length']
averageWordLength_NIRs = input_df_NIR['average word length']
createHistogramWithKDE(averageWordLength_IRs, averageWordLength_NIRs, "Ø Word Length", "# of Reviews", "./Arbeitspakete/AP2_Analyse/Plots/Analysis/H2_Distribution_AverageWordLength.png")
checkVariance(averageWordLength_IRs, averageWordLength_NIRs)
calculateMannWhitneyUtest(averageWordLength_IRs, averageWordLength_NIRs, "less", "2: Average Word Length")
getQuantiles(averageWordLength_IRs, "IR")
getQuantiles(averageWordLength_NIRs, "NIR")

# Test H3
reviewLengths_IRs = input_df_IR['review length']
reviewLengths_NIRs = input_df_NIR['review length']
createHistogramWithKDE(reviewLengths_IRs, reviewLengths_NIRs, "Ø Review Length", "# of Reviews", "./Arbeitspakete/AP2_Analyse/Plots/Analysis/H3_Distribution_AverageReviewLength.png")
checkNormality(reviewLengths_IRs, reviewLengths_NIRs)
checkVariance(reviewLengths_IRs, reviewLengths_NIRs)
calculateMannWhitneyUtest(reviewLengths_IRs, reviewLengths_NIRs, "greater", "3: Review Length")
getQuantiles(reviewLengths_IRs, "IR")
getQuantiles(reviewLengths_NIRs, "NIR")

# Test H5
objectivity_IRs = input_df_IR['objectivity']
objectivity_NIRs = input_df_NIR['objectivity']
createHistogramWithKDE(objectivity_IRs, objectivity_NIRs, "Share of Non-Emotional Words in %", "# of Reviews", "./Arbeitspakete/AP2_Analyse/Plots/Analysis/H5_Distribution_ShareEmotionalWords.png")
checkVariance(objectivity_IRs, objectivity_NIRs)
calculateMannWhitneyUtest(objectivity_IRs, objectivity_NIRs, "less", "5: Objectivity")
getQuantiles(objectivity_IRs, "IR")
getQuantiles(objectivity_NIRs, "NIR")

print("Program finished!")