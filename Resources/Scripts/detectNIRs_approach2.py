import pandas as pd
import os 

output_df = pd.DataFrame(columns=["review id", "genre", "review content"])

for file in os.listdir("./Arbeitspakete/AP2_Analyse/csv_reviews_extended/"):
    if file.endswith("csv"):
        with open("./Arbeitspakete/AP2_Analyse/csv_reviews_extended/" + file, "rb") as f1:
            print(f"Process file {file}")
            genre = file[len("LOBOV5_tokenstream_"):-len(".csv")] 
            input_df = pd.read_csv(f1, sep=",", header=0)
            df_non_incentivized = input_df.query("reviewIsIncentivized == 0")
            for index, row in df_non_incentivized.iterrows():
                if index <= 4:
                    output_df.loc[len(output_df.index)] = row['review id'], genre, row['review content']
                    print(index, row)

output_df.to_csv("./Arbeitspakete/AP2_Analyse/NIR detection_approach2_accuracy.csv", header=True, index=False)
print("program finished!")