import pandas as pd
import spacy

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000

def addReviewLengthToReview(input_file_path):
    input_df = pd.read_csv(input_file_path, sep=",", header=0)
    input_df['review length'] = ''
    list_non_word_POS_tags = ["PUNCT", "NUM", "SYM", "X", "EOL", "SPACE"]
    for index, row in input_df.iterrows():
        print(index)
        word_counter = 0
        doc = nlp(row["review content"], disable=["ner"])
        for token in doc:
            if token.pos_ not in list_non_word_POS_tags:
                word_counter += 1
        input_df.loc[index, "review length"] = word_counter
    input_df.to_csv(input_file_path, sep=",", index=False, header=True)
    
input_path_IR = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv"
input_path_NIR = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv"

addReviewLengthToReview(input_path_IR)
addReviewLengthToReview(input_path_NIR)
print("Program finished!")