import pandas as pd

def computeDescriptives(input_df, descriptives_df, review_type):
    
    new_row = [review_type, 'mean', round(input_df['sentiment_aap'].mean(), 4), round(input_df['average word length'].mean(), 4), round(input_df['review length'].mean(), 4), round(input_df['StarRating'].mean(),4 ), round(input_df['objectivity'].mean(), 4)]
    descriptives_df.loc[len(descriptives_df.index)] = new_row

    new_row = [review_type, 'std', round(input_df['sentiment_aap'].std(), 4), round(input_df['average word length'].std(), 4), round(input_df['review length'].std(), 4), round(input_df['StarRating'].std(),4 ), round(input_df['objectivity'].std(), 4)]
    descriptives_df.loc[len(descriptives_df.index)] = new_row
    
    return descriptives_df

IR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv"
NIR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv"

descriptives_df = pd.DataFrame(columns=['review type', 'measure', 'h1_sentiment', 'h2_complexity', 'h3_elaborateness', 'h4_extremity', 'h5_objectivity'])

input_df_IR = pd.read_csv(IR_path, sep=",", header=0)
input_df_NIR = pd.read_csv(NIR_path, sep=",", header=0)

descriptives_df = computeDescriptives(input_df_IR, descriptives_df, "IR")
descriptives_df = computeDescriptives(input_df_NIR, descriptives_df, "NIR")
descriptives_df.to_csv("./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/descriptiveOverview_romance.csv", index=False, header=True)

print("Program finished!")