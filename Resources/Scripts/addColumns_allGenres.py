import pandas as pd
import os 
import spacy

# Load the German model into spaCy
nlp = spacy.load("de_core_news_sm")

# function to add a column indicating the review type
def add_review_type(input_df, file):
    input_df['reviewType'] = ''
    for index, row in input_df.iterrows():
        if "Kurzmeinung" in row['review content']:
            if (len(row['review content']) < 140):
                input_df.loc[index, 'reviewType'] = 1 # type 1 reviews
            else:
                input_df.loc[index, 'reviewType'] = 2 # type 2 reviews
        else:
            input_df.loc[index, 'reviewType'] = 3 # type 3 reviews
    input_df.to_csv("./Data/csv-reviews_extended/" + file, index=False, header=True)
    print(f"added column to file {file}")

# function to add a column indicating wether a review is incentivized
def add_incentivization_status(input_df, file):
    input_df['reviewIsIncentivized'] = '' 
    input_df['incentive term'] = ''
    for index, row in input_df.iterrows():
        # check for empty cell only to avoid overriding in case there are multiple disclosures in one review
        if input_df.loc[index, 'reviewIsIncentivized'] == '': 
            if "Rezensionsexemplar" in row['review content']:
                input_df.loc[index, 'reviewIsIncentivized'] = 1
                input_df.loc[index, 'incentive term'] = "Rezensionsexemplar"
            elif "Reziexemplar" in row['review content']:
                input_df.loc[index, 'reviewIsIncentivized'] = 1
                input_df.loc[index, 'incentive term'] = "Reziexemplar"
            elif "Rezi-Exemplar" in row['review content']:
                input_df.loc[index, 'reviewIsIncentivized'] = 1
                input_df.loc[index, 'incentive term'] = "Rezi-Exemplar"
            elif "NetGalley" in row['review content']:
                input_df.loc[index, 'reviewIsIncentivized'] = 1
                input_df.loc[index, 'incentive term'] = "NetGalley"
            elif "Leseexemplar" in row['review content']:
                input_df.loc[index, 'reviewIsIncentivized'] = 1
                input_df.loc[index, 'incentive term'] = "Leseexemplar"
            elif "Lese-Exemplar" in row['review content']:
                input_df.loc[index, 'reviewIsIncentivized'] = 1
                input_df.loc[index, 'incentive term'] = "Lese-Exemplar"
            elif "Freiexemplar" in row['review content']:
                input_df.loc[index, 'reviewIsIncentivized'] = 1
                input_df.loc[index, 'incentive term'] = "Freiexemplar"
            else:
                input_df.loc[index, 'reviewIsIncentivized'] = 0
                input_df.loc[index, 'incentive term'] = 0
    input_df.to_csv("./Data/csv_reviews_extended/" + file, index=False, header=True)
    print(f"added column to file {file}")

for file in os.listdir("./Data/csv-reviews_extended/"):
    if file.endswith("csv"):
        with open("./Data/csv-reviews_extended/" + file, "rb") as f1:
            print(f"Process file {file}")
            input_df = pd.read_csv(f1, sep=",", header=0)
            add_review_type(input_df, file)
            add_incentivization_status(input_df, file)
print("Program finished!")
