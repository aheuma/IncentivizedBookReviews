import pandas as pd
import os 

output_df = pd.DataFrame(columns=["Genre", "text_id", "Disclosure Term", "Review Content"])

for file in os.listdir("./Data/csv_reviews_extended/"):
    if file.endswith("csv"):
        with open("./Data/csv_reviews_extended/" + file, "rb") as f1:
            genre = file[len("LOBOV5_review level_"):-len(".csv")] 

            input_df = pd.read_csv(f1, sep=",", names=["text_id", "review content", "review type"])

            counter_reziex = 0
            counter_freiex = 0
            counter_dank = 0
            counter_netgalley = 0
            counter_werbung = 0
            counter_anzeige = 0

            counter_leseexemplar = 0
            counter_leseexemplar_2 = 0
            counter_reziexemplar = 0
            counter_reziexemplar_2 = 0
            counter_vorablesen = 0

            for index, row in input_df.iterrows():
                if "Rezensionsexemplar" in row["review content"] and counter_reziex <= 5:
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Rezensionsexemplar", row['review content']]
                    counter_reziex += 1
                if "Freiexemplar" in row["review content"] and counter_freiex <= 5:
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Freiexemplar", row['review content']]
                    counter_freiex += 1
                if "Vielen Dank" in row["review content"] and counter_dank <= 5:
                    counter_dank += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Dank", row['review content']]
                if "NetGalley" in row["review content"] and counter_netgalley <= 5:
                    counter_netgalley += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "NetGalley", row['review content']]
                if "Werbung" in row["review content"] and counter_werbung <= 5:
                    counter_werbung += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Werbung", row['review content']]
                if "Anzeige" in row["review content"] and counter_anzeige <= 5:
                    counter_anzeige += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Anzeige", row['review content']]
                if "Leseexemplar" in row["review content"] and counter_leseexemplar <= 5:
                    counter_leseexemplar += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Leseexemplar", row['review content']]
                if "Lese-Exemplar" in row["review content"] and counter_leseexemplar_2 <= 5:
                    counter_leseexemplar_2 += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Lese-Exemplar", row['review content']]
                if "Reziexemplar" in row["review content"] and counter_reziexemplar <= 5:
                    counter_reziexemplar += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Reziexemplar", row['review content']]
                if "Rezi-Exemplar" in row["review content"] and counter_reziexemplar_2 <= 5:
                    counter_reziexemplar_2 += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Rezi-Exemplar", row['review content']]
                if "Vorablesen" in row["review content"] and counter_vorablesen <= 5:
                    counter_vorablesen += 1
                    output_df.loc[len(output_df.index)] = [genre, row["text_id"], "Vorablesen", row['review content']]
            print(f"Finished searching genre: {genre}")                            

output_df.to_csv("IR detection_disclosure terms_1.csv", index=False)
output_df.to_csv("IR detection_disclosure terms_2.csv", index=False)
print("Program finished!")
