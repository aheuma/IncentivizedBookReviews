import pandas as pd

input_df_IR = pd.read_csv("./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_IRs_prep.csv", sep=",", header=0)
input_df_NIR = pd.read_csv("./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_NIRs_prep.csv", sep=",", header=0)

output_file_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/Analysis/LOBOV5_liebesroman_ALL_prep.csv"

output_df = pd.concat([input_df_IR, input_df_NIR])

output_df.to_csv(output_file_path, index=False, header=True, columns=["review id", "reviewIsIncentivized", "sentiment_aap", "average word length", "review length", "StarRating", "objectivity"])
print("Program finished!")