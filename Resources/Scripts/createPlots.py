import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import pandas as pd


def createBarPlot(labels, values, xlabel, ylabel, file_path):
    plt.figure(figsize=(10, 6))
    plt.bar(labels, values)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    for i, value in enumerate(values):
        plt.text(i, value + 1, str(value), ha='center', fontsize=8)
    plt.xticks(rotation=30, ha='right')
    plt.subplots_adjust(bottom=0.2)
    #plt.show()
    plt.savefig(file_path, dpi=300, bbox_inches='tight')
    print("Plot saved!")

def create_IR_share_bar_plot(dict_incentivization_per_genre):
    # Prepare data for plotting based on sorted genres
    total_reviews = [dict_incentivization_per_genre[genre][0] for genre in dict_incentivization_per_genre]
    incentivized_reviews = [dict_incentivization_per_genre[genre][2] for genre in dict_incentivization_per_genre]

    # Calculate relative shares
    incentivized_percentage = [(incentivized_reviews[i] / total_reviews[i]) * 100 for i in range(len(dict_incentivization_per_genre))]

    # Plotting the data
    x = np.arange(len(dict_incentivization_per_genre))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize=(10,6))
    bars = ax.bar(x, incentivized_percentage, width)

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Genres')
    ax.set_ylabel('Share in %')
    ax.set_xticks(x)
    ax.set_xticklabels(dict_incentivization_per_genre, rotation=30, ha='right')  # Use sorted genres for x-axis labels

    # Function to add labels to the bars with more vertical offset, rotation, and adjusted font size
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 10),  # offset to avoid overlap
                        textcoords="offset points",
                        ha='center', va='bottom',
                        fontsize=7,
                        rotation=30)  # Rotate the labels for better readability

    # Add labels
    add_labels(bars)

    # Increase space at the top and bottom
    plt.subplots_adjust(top=0.75, bottom=0.2)

    # Adjust y-axis limit to add more space above the highest bar
    ax.set_ylim(0, max(incentivized_percentage) + 10)
    plt.savefig('./Plots/reviews_IR_shares_ALL.png', dpi=300, bbox_inches='tight')
    print("Plot saved!")

def create_summarized_pie_chart(data):
    total_reviews = sum(data.values())
    threshold_percentage = 3.5
    filtered_genres = {genre: value for genre, value in data.items() if (value / total_reviews * 100) > threshold_percentage}
    remaining_genres = {genre: value for genre, value in data.items() if genre not in filtered_genres}

    labels_combined = list(filtered_genres.keys()) + ['Other Genres']
    values_combined = list(filtered_genres.values()) + [sum(remaining_genres.values())]

    # Farben für die Segmente festlegen
    colors = [plt.cm.tab20c(i) for i in np.arange(len(labels_combined))]

    # Indizes für spezielle Farben festlegen
    other_genres_index = labels_combined.index('Other Genres')

    # Farben anpassen 
    colors[other_genres_index] = 'yellowgreen'

    plt.figure(figsize=(10, 10))
    plt.pie(values_combined, labels=labels_combined, autopct='%1.1f%%', startangle=140, colors=colors)

    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    plt.tight_layout()
    plt.savefig('./Plots/reviews_per_genre_PIE.png', dpi=300, bbox_inches='tight')
    print("Plot saved!")

def create_bar_plot_hu_IR_comparison(dictionary):
    # Extrahieren der Daten
    genres = list(dictionary.keys())
    share1 = [values[0] for values in dictionary.values()]
    share2 = [values[1] for values in dictionary.values()]

    # Anzahl der Genres
    n = len(genres)

    # x-Positionen der Balken
    ind = np.arange(n)

    # Breite der Balken
    width = 0.35

    # Erstellen der Balken
    fig, ax = plt.subplots()
    bar1 = ax.bar(ind - width/2, share1, width, label='LoBo Corpus')
    bar2 = ax.bar(ind + width/2, share2, width, label='Hu et al.')

    # Hinzufügen der Beschriftungen, Titel und Achsenbeschriftungen
    ax.set_ylabel('IR Share (%)')
    ax.set_xticks(ind)
    ax.set_xticklabels(genres)
    ax.legend()

    # Höchsten Wert ermitteln und y-Achse entsprechend anpassen
    max_height = max(max(share1), max(share2))
    ax.set_ylim(0, max_height * 1.1)

    # Hinzufügen der Prozentwerte als Labels über den Balken
    def add_labels(bars):
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.1f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),  # 3 Punkte vertikaler Versatz
                        textcoords="offset points",
                        ha='center', va='bottom')

    add_labels(bar1)
    add_labels(bar2)
    plt.xticks(rotation=30, ha='right')
    plt.subplots_adjust(bottom=0.2)

    # Layout anpassen und Plot anzeigen
    fig.tight_layout()
    #plt.show()

    plt.savefig('./Plots/hu_IR_comparison.png', dpi=300, bbox_inches='tight')
    print("Plot saved!")

def create_reviewType_share_bar_plot(dictionary):
    
    # Calculate the total number of reviews
    total_reviews = sum(dictionary.values())

    # Calculate the percentage share for each review type
    percentages = {k: (v / total_reviews) * 100 for k, v in dictionary.items()}

    # Plotting
    plt.figure(figsize=(10, 6))
    bars = plt.bar(percentages.keys(), percentages.values(), color=['skyblue', 'lightgreen', 'lightcoral'])

    # Adding title and labels
    plt.xlabel('Review Type')
    plt.ylabel('Percentage (%)')
    plt.xticks(rotation=30, ha='right')
    plt.subplots_adjust(bottom=0.2)

    # Adjust the y-axis limits to provide more space above the highest bar
    max_value = max(percentages.values())
    plt.ylim(0, max_value + max_value * 0.1)  # Increase the upper limit by 10%

    # Displaying the percentage value on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + max_value * 0.02, f'{height:.2f}%', ha='center')

    # Show the plot
    plt.savefig('./Plots/review_type_shares_romance.png', dpi=300, bbox_inches='tight')
    print("Plot saved!")


# total number of reviews per genre
dict_all_reviews_per_genre = {
    "jugendbuch": 243731, 
    "krimi-thriller": 240131, 
    "fantasy": 131101, 
    "liebesroman": 130256,
    "romane": 75604,
    "kinderbuch": 64874,
    "sachbuch": 62236,
    "erotische-literatur": 46367,
    "historische-romane": 45362,
    "science-fiction": 16648,
    "biografie": 19474,
    "humor": 18462,
    "comic": 12628,
    "klassiker": 13560,
    "gedichte-drama": 3198,
    "NaN": 66301}

dict_all_reviews_per_genre = dict(sorted(dict_all_reviews_per_genre.items(), key=lambda item: item[1], reverse=True))
labels_Totals = list(dict_all_reviews_per_genre.keys())
values_Totals = list(dict_all_reviews_per_genre.values())


# Total reviews = [0]
# Rezension = [1]
# Kurzmeinung = [2]
dict_review_types = {
    "jugendbuch": [243731, 95255, 148476], 
    "krimi-thriller": [240131, 115132, 124999], 
    "fantasy": [131101, 62567, 68534], 
    "liebesroman": [130256, 51635, 78621],
    "romane": [75604, 36857, 38747],
    "kinderbuch": [64874, 29697, 35177],
    "sachbuch": [62236, 34579, 27657],
    "erotische-literatur": [46367, 16552, 29815],
    "historische-romane": [45362, 23737, 21625],
    "science-fiction": [16648, 6701, 9947],
    "biografie": [19474, 9919, 9555],
    "humor": [18462, 8929, 9533],
    "comic": [12628, 5862, 6766],
    "klassiker": [13560, 6837, 6723],
    "gedichte-drama": [3198, 1770, 1428],
    "NaN": [66301, 33128, 33173]}

dict_review_types = dict(sorted(dict_review_types.items(), key=lambda item: item[1], reverse=True))
labels_review_types = list(dict_review_types.keys())
values_review_types = np.array(list(dict_review_types.values()))

# [0] = total reviews
# [1] = NIRs
# [2] = IRs
dict_incentivization_per_genre = {
    "erotische-literatur": [46367, 43760, 2607],
    "liebesroman": [130256, 125381, 4875],
    "science-fiction": [16648, 16226, 422],
    "fantasy": [131101, 128334, 2767], 
    "NaN": [66301, 64968, 1333],
    "jugendbuch": [243731, 239357, 4374],
    "romane": [75604, 74567, 1037],
    "kinderbuch": [64874, 64020, 854],
    "historische-romane": [45362, 44788, 574],
    "gedichte-drama": [3198, 3160, 38],
    "krimi-thriller": [240131, 237317, 2814], 
    "humor": [18462, 18257, 205],        
    "sachbuch": [62236, 61572, 664],
    "comic": [12628, 12496, 132],    
    "biografie": [19474, 19298, 176],        
    "klassiker": [13560, 13535, 25]}

# absolute IR numbers
dict_IRs_per_genre = {
    "jugendbuch": 4374, 
    "krimi-thriller": 2814, 
    "fantasy": 2767, 
    "liebesroman": 4875,
    "romane": 1037,
    "kinderbuch": 854,
    "sachbuch": 664,
    "erotische-literatur": 2607,
    "historische-romane": 574,
    "science-fiction": 422,
    "biografie": 176,
    "humor": 205,
    "comic": 132,
    "klassiker": 25,
    "gedichte-drama": 38,
    "NaN": 1333}

dict_IRs_per_genre = dict(sorted(dict_IRs_per_genre.items(), key=lambda item: item[1], reverse=True))
labels_IRs = list(dict_IRs_per_genre.keys())
values_IRs = list(dict_IRs_per_genre.values())

dict_NIRs_per_genre = {
    "jugendbuch": 239381, 
    "krimi-thriller": 237343, 
    "fantasy": 128354, 
    "liebesroman": 125393,
    "romane": 74573,
    "kinderbuch": 64022,
    "sachbuch": 61576,
    "erotische-literatur": 43762,
    "historische-romane": 44791,
    "science-fiction": 16226,
    "biografie": 19299,
    "humor": 18258,
    "comic": 12497,
    "klassiker": 13536,
    "gedichte-drama": 3160,
    "NaN": 64970}

dict_NIRs_per_genre = dict(sorted(dict_NIRs_per_genre.items(), key=lambda item: item[1], reverse=True))
labels_NIRs = list(dict_NIRs_per_genre.keys())
values_NIRs = list(dict_NIRs_per_genre.values())
label_romance = ["Kurzmeinung", "Rezension"]
value_romance = [78621, 51635]

# LoBo = [0]
# Hu et al = [1]
dict_hu_IR_comparison = {
    "Young Adult": [1.795, 7.256],
    "Crime & Thriller": [1.172, 9.351],
    "Fantasy": [2.111, 7.784],
    "Romance": [3.743, 13.721],
    "Children": [1.316, 5.98],
    "History & Biography": [1.157, 6.797],
    "Comic": [1.045, 4.37]
    }

# Total reviews = [0]
# Kurzmeinung = [1]
# Kurzmeinung & Rezension = [2]
# Rezension = [3]
dict_review_types_romance = {"Kurzmeinungen": 20479,
                             "Kurzmeinungen \n & Rezensionen": 58142,
                             "Rezensionen": 51635}
labels_review_types_romance = list(dict_review_types_romance.keys())
values_review_types_romance = list(dict_review_types_romance.values())

# Year = [0]
# Number of Reviews = [1]
metadata_df = pd.read_pickle("./Arbeitspakete/AP2_Analyse/LOBOV5_metadata.pkl")
series_review_years = metadata_df['text_rez_year'].value_counts()
dict_review_years = series_review_years.to_dict()
del dict_review_years['unknown']
dict_review_years = dict(sorted(dict_review_years.items(), key=lambda item: item[1], reverse=True))
labels_review_years = list(dict_review_years.keys())
values_review_years = list(dict_review_years.values())

#create_summarized_pie_chart(dict_all_reviews_per_genre)
#createBarPlot(labels_IRs, values_IRs, "Genres", "# of Reviews", "./Plots/reviews_IRs_absolute_per_genre_BAR.png")
#createBarPlot(labels_Totals, values_Totals, "Genres", "# of Reviews", "./Plots/total_reviews_per_genre_BAR.png")
#createBarPlot(labels_NIRs, values_NIRs, "Genres", "# of Reviews", "./Plots/reviews_NIRs_per_genre_BAR.png")
#create_bar_plot_hu_IR_comparison(dict_hu_IR_comparison)
#create_IR_share_bar_plot(dict_incentivization_per_genre)
#create_reviewType_share_bar_plot(dict_review_types_romance)
