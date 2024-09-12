import pandas as pd

def addStarRatingToReview(file_path, metadata_df):
    input_df = pd.read_csv(file_path, sep=",", encoding="utf-8", header=0)
    input_df['StarRating'] = ''
    metadata_dict = metadata_df.set_index('text_id')['text_rez_rating'].to_dict()
    for index, row in input_df.iterrows():
        print(index)
        review_id = row['review id']
        star_rating = int(metadata_dict.get(review_id, None))
        input_df.loc[index, 'StarRating'] = star_rating
    input_df.to_csv(file_path, index=False, header=True)

'''
metadata_df = pd.read_csv("./Arbeitspakete/AP2_Analyse/LOBOV5_metadata.csv", sep=",", encoding="utf-8", header=0)
metadata_df.to_pickle("./Arbeitspakete/AP2_Analyse/LOBOV5_metadata.pkl")
'''

metadata_df = pd.read_pickle("./Arbeitspakete/AP2_Analyse/LOBOV5_metadata.pkl")
IR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv"
NIR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv"

addStarRatingToReview(IR_path, metadata_df)
addStarRatingToReview(NIR_path, metadata_df)

print("Finished!")