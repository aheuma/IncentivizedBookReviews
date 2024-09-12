import pandas as pd
import os
import spacy
from spacy.matcher import DependencyMatcher

nlp = spacy.load("de_core_news_sm")
output_df = pd.DataFrame(columns=["Genre", "text_id", "review content"])

dep_matcher = DependencyMatcher(nlp.vocab)
dep_pattern = [
    {
        "RIGHT_ID": "gekauft",
        "RIGHT_ATTRS": {"ORTH": "gekauft", "POS": "VERB"}
    },
    {
        "LEFT_ID": "gekauft",
        "REL_OP": ">",
        "RIGHT_ID": "buch",
        "RIGHT_ATTRS": {"ORTH": "Buch"}
    }
]

dep_matcher.add("IHaveBoughtPattern", [dep_pattern])

def find_purchase_intentions(doc):
    dep_matches = dep_matcher(doc)
    return len(dep_matches) != 0

for file in os.listdir("./Data/csv_reviews_extended/"):
    if file.endswith("csv"):
        with open(os.path.join("./Data/csv_reviews_extended/", file), "r", encoding="utf-8") as f1:
            genre = file[len("LOBOV5_review level_"):-len(".csv")]

            input_df = pd.read_csv(f1, sep=",", names=["text_id", "review content", "review type", "incentivized", "incentive term"])
            input_df['purchase intention'] = ''
            counter_purchaseIntention = 0

            # Use nlp.pipe to process texts in batches
            reviews = input_df["review content"].tolist()
            docs = nlp.pipe(reviews, batch_size=50)

            for index, (row, doc) in enumerate(zip(input_df.itertuples(), docs)):
                if counter_purchaseIntention > 5:
                    break
                if find_purchase_intentions(doc):
                    output_df.loc[len(output_df.index)] = [genre, row.text_id, row._2]  # row._2 corresponds to 'review content'
                    counter_purchaseIntention += 1
            print(f"Finished searching genre: {genre}")

output_df.to_csv("NIR detection_approach1DepMatch_accuracy.csv", index=False)
print("Program finished!")
