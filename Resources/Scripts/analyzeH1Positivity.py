import spacy
import pandas as pd

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000

def addAAPToReview(input_path):
    input_df = pd.read_csv(input_path, sep=",", header=0)
    input_df['sentiment_aap'] = ''
    df_sentiArt = pd.read_excel("./Arbeitspakete/AP2_Analyse/Scripts/6.2_Analysis/120kSentiArt_DE.xlsx")
    df_sentiArt.drop(columns=["ang_z", "fear_z", "disg_z", "hap_z", "sad_z", "surp_z"], inplace=True) # drop discrete emotions' scores

    sentiArt_dict = pd.Series(df_sentiArt.AAPz.values, index=df_sentiArt.wordLC).to_dict()
    
    list_content_words = ["ADJ", "ADV", "INTJ", "NOUN", "PROPN", "VERB"]
    # Start sentiArt-ing
    for index, row in input_df.iterrows():
        print(index)
        review = nlp(str(row['review content']), disable=["ner"]) # exclude named entity recognition to fasten computing
        review_aap = 0
        token_counter = 0
        for token in review:
            if token.pos_ in list_content_words: # calculate sentiment score only in case token is content word
                token_counter += 1
                token_lower = str(token.text).lower()
                current_token_aap = sentiArt_dict.get(token_lower, 0)
                review_aap += current_token_aap
        average_review_aap = round((review_aap / token_counter), 3)
        input_df.loc[index, 'sentiment_aap'] = average_review_aap
    input_df.to_csv(input_path, index=False, header=True)

IR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv"
NIR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv"

addAAPToReview(IR_path)
addAAPToReview(NIR_path)
            
print("program finished succesfully!")
