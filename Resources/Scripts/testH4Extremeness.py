import pandas as pd 
import numpy as np
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

def conductChiSquareTest(contingency_table):
    # Check expected frequencies
    chi2, p_value, dof, expected = chi2_contingency(contingency_table)

    print("Contingency table:")
    print(contingency_table)
    print("\nExpetcted frequencies:")
    print(expected)

    # Interpretation of expected frequencies-test
    if np.all(expected >= 5): # Prerequisite of Chi-Square = expected > 5
        print("\nAll expected frequencies are >= 5. Prerequisites are fulfilled.")
    else:
        print("\Some expected frequencies are < 5.")

    # Conduct Chi-Square-Test
    print("\nChi-Square-Test:")
    print(f"Chi-Square-Value: {round(chi2, 4)}")
    print(f"p-Value: {round(p_value, 4)}")
    print(f"Degrees of freedom: {dof}")

    # Calculate effect size
    n = np.sum(contingency_table)  # total sample size
    min_dim = min(contingency_table.shape) - 1  # minimum of (k-1, r-1)
    cramers_v = np.sqrt(chi2 / (n * min_dim))
    print(f"Cramers V (effect size): {cramers_v}")

def createStackedBarPlot(contingency_table):
    contingency_table.plot(kind='bar', stacked=True, color=['#E54E35', '#FDBB6C', '#FEFFBE', '#B3DF72', '#3FAA59'])
    plt.xlabel('Review Type')
    plt.ylabel('Share in %')
    plt.legend(title='Star Rating')
    plt.xticks(rotation=30, ha='right')
    plt.yticks(np.arange(0, 101, 10))
    plt.subplots_adjust(bottom=0.2)
    plt.savefig("./Arbeitspakete/AP2_Analyse/Plots/Analysis/H4_StarRatingDistribution_relative.png", dpi=300, bbox_inches='tight')

IR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv"
NIR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv"

IR_df = pd.read_csv(IR_path, sep=",", header=0) 
NIR_df = pd.read_csv(NIR_path, sep=",", header=0)

IR_df['ReviewType'] = "IR"
NIR_df['ReviewType'] = "NIR"

all_reviews_df = pd.concat([IR_df, NIR_df], ignore_index=True)

# Create contingency table
contingency_table = pd.crosstab(all_reviews_df['ReviewType'], all_reviews_df['StarRating'])

# Create additional contingency table with relative frequencies
relative_frequencies = contingency_table.div(contingency_table.sum(axis=1), axis=0) * 100
relative_frequencies = round(relative_frequencies, 3)

print("Contingency table (relative frequencies):")
print(relative_frequencies)

conductChiSquareTest(contingency_table)
createStackedBarPlot(relative_frequencies)

print(f"IR median: {IR_df['StarRating'].mean()}")
print(f"NIR median: {NIR_df['StarRating'].mean()}")