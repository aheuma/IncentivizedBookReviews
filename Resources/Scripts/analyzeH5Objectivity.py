import pandas as pd

def computeObjectivityScore(LIWC_path):
    liwc_df = pd.read_csv(LIWC_path, sep=",", header=0)
    liwc_df['objectivity'] = ''
    for index, row in liwc_df.iterrows():
        print(index)
        objectivity_score = 100 - (row['posemo'] + row['negemo'])
        liwc_df.loc[index, 'objectivity'] = objectivity_score
    liwc_df.to_csv(LIWC_path, index=False, header=True)

def addObjectivityScoreToReview(file_path, LIWC_path):
    input_df = pd.read_csv(file_path, sep=",", header=0)
    liwc_df = pd.read_csv(LIWC_path, sep=",", header=0)
    liwc_dict = liwc_df.set_index('review id')['objectivity'].to_dict()
    for index, row in input_df.iterrows():
        print(index)
        review_id = row['review id']
        objectivity_score = float(liwc_dict.get(review_id, None))
        input_df.loc[index, 'objectivity'] = objectivity_score
    input_df.to_csv(file_path, index=False, header=True)

IR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv"
NIR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv"

IR_LIWC_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_LIWC Analysis.csv"
NIR_LIWC_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_LIWC Analysis.csv"

computeObjectivityScore(IR_LIWC_path)
computeObjectivityScore(NIR_LIWC_path)

addObjectivityScoreToReview(IR_path, IR_LIWC_path)
addObjectivityScoreToReview(NIR_path, NIR_LIWC_path)
print("Program finished!")