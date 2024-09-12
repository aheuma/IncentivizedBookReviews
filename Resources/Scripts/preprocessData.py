import pandas as pd
import re
import spacy
from spacy import Language

nlp = spacy.load("de_core_news_sm")
nlp.max_length = 2000000

# Modify spacy sentence boundaries
@Language.component("set_custom_boundaries")
def set_custom_boundaries(doc):
    for token in doc:
        token.is_sent_start = False
    return doc

nlp.add_pipe("set_custom_boundaries", before="parser")

#Function to check the POS-tag of special characters and emojis
def checkSpecialCharacters(input_file):
    with open(input_file, "r", encoding="utf-8") as file:
        file_contents = file.read()
        doc = nlp(file_contents)
        for token in doc:
            print(token, token.pos_)

# Function to delete Emoticons and special characters
def deleteEmojisAndHashtag(input_df, output_path):
    for index, row in input_df.iterrows():
        review_content = row['review content']
        review_content = review_content.replace("❤️", "")
        review_content = review_content.replace("♥", "")
        review_content = review_content.replace("♡", "")
        review_content = review_content.replace("★", "")
        review_content = review_content.replace("*", "")
        review_content = review_content.replace("☆", "")
        review_content = review_content.replace("xD", "")
        review_content = review_content.replace("XD", "")
        review_content = review_content.replace("�", "")
        review_content = review_content.replace("<3", "")
        review_content = review_content.replace("⭐", "")
        review_content = review_content.replace("✔", "")
        review_content = review_content.replace("●", "")
        review_content = review_content.replace(": - )", "")
        review_content = review_content.replace(": - (", "")
        review_content = review_content.replace("; - )", "")
        review_content = review_content.replace("❇️", "")
        review_content = review_content.replace("#", "")
        review_content = review_content.replace("~", "")
        review_content = review_content.replace("✦", "")
        input_df.at[index, 'review content'] = review_content
    input_df.to_csv(output_path, index=False, header=True)
    print("Finished deleting emojis!")

# Function to delete URL parts
def deleteURLs(input_df, output_path):
    for index, row in input_df.iterrows():
        review_content = row['review content']
        review_content = review_content.replace("https : ", "")
        review_content = review_content.replace("http : ", "")
        url_pattern_1 = r"\/?([a-z]+-)+[a-z]+\/" # matches hyphenated url parts, e.g. rezi-buch
        url_pattern_2 = r"(https?:\/+)?(www\.)?([a-z]|[0-9])+\.(com|de|at)(\/([a-z]+|[0-9]+))?\/?"

        review_content = re.sub(url_pattern_1, "", review_content)
        review_content = re.sub(url_pattern_2, "", review_content)

        input_df.at[index, 'review content'] = review_content
    input_df.to_csv(output_path, index=False, header=True)
    print("Finished deleting URLs!")

# Function to delete the review type-indicator
def deleteReviewTypeIndicator(input_df, output_path):
    for index, row in input_df.iterrows():
        review_content = row['review content']
        pattern_kurzmeinung = r"^Kurzmeinung "
        review_content = re.sub(pattern_kurzmeinung, "", review_content)
        review_content = re.sub(r"^: ", "", review_content)
        input_df.at[index, 'review content'] = review_content
    input_df.to_csv(output_path, index=False, header=True)
    print("Finished deleting review type indicators!")

# Function to unify quotation marks in reviews
def unifyQuotationMarks(input_df, output_path):
    for index, row in input_df.iterrows():
        review_content = row['review content']

        review_content = review_content.replace("»", "\"") #fr
        review_content = review_content.replace("«", "\"") #fr
        review_content = review_content.replace("„", "\"") #de
        review_content = review_content.replace("“", "\"") #de
        review_content = review_content.replace("”", "\"") #en
         
        input_df.at[index, 'review content'] = review_content
    input_df.to_csv(output_path, index=False, header=True)
    print("Finished unifying quotation marks!")

input_character_file = "./Arbeitspakete/AP2_Analyse/Example_Special_Characters.txt"
IR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/LOBOV5_liebesroman_IRs_prep.csv"
NIR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/LOBOV5_liebesroman_NIRs_prep.csv"
input_df_IR_prep = pd.read_csv(IR_path, sep=",", encoding="utf-8", header = 0)
input_df_NIR_prep = pd.read_csv(NIR_path, sep=",", encoding="utf-8", header = 0)

deleteEmojisAndHashtag(input_df_IR_prep, IR_path)
deleteURLs(input_df_IR_prep, IR_path)
deleteReviewTypeIndicator(input_df_IR_prep, IR_path)
unifyQuotationMarks(input_df_IR_prep, IR_path)

deleteEmojisAndHashtag(input_df_NIR_prep, NIR_path)
deleteURLs(input_df_NIR_prep, NIR_path)
deleteReviewTypeIndicator(input_df_NIR_prep, NIR_path)
unifyQuotationMarks(input_df_NIR_prep, NIR_path)

print("Program finished!")
