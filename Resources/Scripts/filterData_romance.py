import pandas as pd

input_file = "./Data/liebesroman-corpus/LOBOV5_tokenstream_liebesroman.csv"

output_df = pd.DataFrame(columns=["review id", "review content", "reviewIsIncentivized", "incentive term", "reviewType", "reviewIsGerman"])

with open(input_file, "rb") as file:
    input_df = pd.read_csv(file, sep=",", header=0)

    # Exclude all reviews with ReviewType = 1
    df_without_type1Kurzmeinungen = input_df.query("reviewType != 1")
    df_without_type1Kurzmeinungen.to_csv(input_file, index=False, header=True)

    # Exclude all non-German reviews
    df_without_nongermans = input_df.query("reviewIsGerman == 1")
    df_without_nongermans.to_csv(input_file, index=False, header=True)
    
    # Create separate csv-file with all IRs only
    df_IRs = input_df.query("reviewIsIncentivized == 1").copy()
    df_IRs.to_csv("./Data/liebesroman-corpus/LOBOV5_liebesroman_IRs.csv", index=False, header=True)

    # Create separate csv-file with equal number of NIRs
    df_NIRs = input_df.query("reviewIsIncentivized == 0").copy()
    output_df = df_NIRs.sample(n=df_IRs["review id"].nunique(), random_state=42)    
    output_df.to_csv("./Data/liebesroman-corpus/LOBOV5_liebesroman_NIRs.csv", index=False, header=True)    

    print(f"Länge IR: {df_IRs['review id'].nunique()}")
    print(f"Länge NIR: {output_df['review id'].nunique()}")
print("Program finished!")
