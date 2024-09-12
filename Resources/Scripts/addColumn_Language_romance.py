import pandas as pd
import langid

def detect_language(text):
    # langid.classify returns a tuple (language_code, confidence)
    return langid.classify(text)[0]

input_file = "./Data/liebesroman-corpus/LOBOV5_tokenstream_liebesroman.csv"

with open(input_file, "rb") as file:
    input_df = pd.read_csv(file, sep=",", header=0)
    input_df["reviewIsGerman"] = ""
    for index, row in input_df.iterrows():
        print(index)
        if detect_language(row['review content']) != "de":
            input_df.loc[index, "reviewIsGerman"] = 0
        else:
            input_df.loc[index, "reviewIsGerman"] = 1
    input_df.to_csv(input_file, index=False, header=True)
    print(f"Non-Germans: {len(input_df.query('reviewIsGerman == 0'))}")
print("Program finished!")
