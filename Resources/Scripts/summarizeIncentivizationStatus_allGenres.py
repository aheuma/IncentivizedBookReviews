import pandas as pd
import os 

# function to summarize number of (non-)incentivized reviews 
def sum_incentivization_status(genre, input_df, output_df):
    # change data type to numeric
    input_df['reviewIsIncentivized'] = pd.to_numeric(input_df['reviewIsIncentivized'])
    counter_reviews_total = input_df['review id'].nunique()
    df_incentivized = input_df.query("reviewIsIncentivized == 1")
    counter_IRs = len(df_incentivized['reviewIsIncentivized'])
    df_non_incentivized = input_df.query("reviewIsIncentivized == 0")
    counter_NIRs = len(df_non_incentivized['reviewIsIncentivized'])
    IR_share = round((counter_IRs / counter_reviews_total) * 100, 3)
    NIR_share = round((counter_NIRs / counter_reviews_total) * 100, 3)
    new_row = [genre, counter_reviews_total, counter_IRs, counter_NIRs, IR_share, NIR_share]
    output_df.loc[len(output_df.index)] = new_row

output_df = pd.DataFrame(columns=["genre", "# reviews", "# IR", "# NIR", "% IR", "% NIR"])

for file in os.listdir("./Data/csv_reviews_extended/"):
    if file.endswith("csv"):
        with open("./Data/csv_reviews_extended/" + file, "rb") as f1:
            # Create filename with genre
            genre = file[len("LOBOV5_tokenstream_"):-len(".csv")] 
            input_df = pd.read_csv(f1, sep=",", header=0)
            sum_incentivization_status(genre, input_df, output_df)

output_df.to_excel("./genre_overview_incentivization.csv", index=False, header=True)
print("Program finished!")
