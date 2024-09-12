import pandas as pd

def getNumberOfBooks(input_df, metadata_df):
    metadata_dict_numberOfBooks = metadata_df.set_index('text_id')['text_book_ID'].to_dict()
    list_book_ids = []
    for index, row in input_df.iterrows():
        review_id = row['review id']
        if review_id in metadata_dict_numberOfBooks:
            list_book_ids.append(metadata_dict_numberOfBooks.get(review_id, None))
    return list_book_ids

def getNumberOfReviewers(input_df, metadata_df):
    metadata_dict_numberOfReviewers = metadata_df.set_index('text_id')['text_rez_user'].to_dict()
    list_reviewer_ids = []
    for index, row in input_df.iterrows():
        review_id = row['review id']
        if review_id in metadata_dict_numberOfReviewers:
            list_reviewer_ids.append(metadata_dict_numberOfReviewers.get(review_id, None))
    return list_reviewer_ids

def getUniqueValues(list, value):
    print(f"Total number with duplicates: {len(list)} {value}")
    list_without_duplicates = pd.Series(list).drop_duplicates().tolist()
    print(f"Total number without duplicates: {len(list_without_duplicates)} {value}")

metadata_df = pd.read_pickle("./Arbeitspakete/AP2_Analyse/LOBOV5_metadata.pkl")
IR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/LOBOV5_liebesroman_IRs.csv"
NIR_path = "./Arbeitspakete/AP2_Analyse/liebesroman-corpus/LOBOV5_liebesroman_NIRs.csv"
IR_df = pd.read_csv(IR_path, sep=",", header=0) 
NIR_df = pd.read_csv(NIR_path, sep=",", header=0)

# Get general meta information
print(metadata_df.columns)
print(len(metadata_df.columns))
print(metadata_df['text_rez_time'].value_counts())
publication_year_month = metadata_df['text_rez_year_month'].value_counts().to_dict()
publication_year_month = dict(sorted(publication_year_month.items(), key=lambda item: item[0], reverse=True))
print(f"Anzahl Bücher: {metadata_df['text_book_ID'].nunique()}")
print(f"Anzahl Rezensenten: {metadata_df['text_rez_user'].nunique()}")
print(metadata_df['text_rez_user'].value_counts())
print(f"Anzahl Rezensionen: {metadata_df['text_id'].nunique()}")

# Get meta-information on IR and NIR samples
book_ids_IR = getNumberOfBooks(IR_df, metadata_df) 
reviewer_ids_IR = getNumberOfReviewers(IR_df, metadata_df)
getUniqueValues(book_ids_IR, "IR-Books")
getUniqueValues(reviewer_ids_IR, "IR-Reviewers")

book_ids_NIR = getNumberOfBooks(NIR_df, metadata_df) 
reviewer_ids_NIR = getNumberOfReviewers(NIR_df, metadata_df)
getUniqueValues(book_ids_NIR, "NIR-Books")
getUniqueValues(reviewer_ids_NIR, "NIR-Reviewers")
