import pandas as pd
import os

# Script creates csv-file with all reviews
# One file per genre
# One row = one review

for file in os.listdir("./Data/csv_tokens/"):
    if file.endswith("csv"):
        with open("./Data/csv_tokens/" + file, "rb") as f1:
            print(f"Creating genre: {f1}")
            df = pd.read_csv(f1, sep=",")
            df.drop(columns=['pos', 'rfpos'], inplace=True)

            df_new = pd.DataFrame(columns=["review id", "review content"])

            review_id_list = []
            unique_review_ids = df['text_id'].unique().tolist()
            for id in unique_review_ids:
                review_id_list.append(id)
            id_counter = 0
            review_id_placeholder = review_id_list[id_counter]

            review_text_placeholder = ""

            review_dict = {}
            for ind in df.index:
                if df['text_id'][ind] == review_id_placeholder: # append text of current review
                    review_text_placeholder += str(df['word'][ind])
                    review_text_placeholder += " "

                    # Add the very last review of csv-file to review-list
                    if ind == len(df['text_id'])-1:
                        review_dict[review_id_placeholder] = review_text_placeholder
                else: # start of a new review
                    id_counter += 1
                    review_id_placeholder = review_id_list[id_counter]
                    review_dict[review_id_placeholder] = review_text_placeholder
                    review_text_placeholder = ""
                    review_text_placeholder += str(df['word'][ind])
                    review_text_placeholder += " "
            
            df_new = pd.DataFrame(list(review_dict.items()), columns=["review id", "review content"])
            df_new.drop_duplicates(inplace=True)
            
            df_new.to_csv("./Data/csv_reviews/" + file, sep=",", index=False, header=True)
print("Program finished!")