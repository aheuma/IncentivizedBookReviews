import spacy
import pandas as pd
import statistics

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000

def addAverageWordLengthToReview(input_path):
    input_df = pd.read_csv(input_path, sep=",", header=0)
    input_df['average word length'] = ''
    for index, row in input_df.iterrows():
        print(index)
        doc = nlp(row['review content'], disable=["ner"])
        list_non_word_POS_tags = ["PUNCT", "NUM", "SYM", "X", "EOL", "SPACE"]
        word_lengths_per_review = []
        for token in doc:
            if token.pos_ not in list_non_word_POS_tags:
                word_lengths_per_review.append(len(token.text))
        average_word_length = round(statistics.mean(word_lengths_per_review), 4)
        input_df.loc[index, 'average word length'] = average_word_length
    input_df.to_csv(input_path, index=False, header=True)

IR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv"
NIR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv"

addAverageWordLengthToReview(IR_path)
addAverageWordLengthToReview(NIR_path)

print("Program finished")