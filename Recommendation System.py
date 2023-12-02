import pandas as pd

# Create a dataset with specified movies
movies_data = {
    'Title': ['Harry Potter', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Prisoner of Azkaban', 'Harry Potter and the Goblet of Fire','Harry Potter and the Order of Phoenix','Harry Potter and the Half-Blood Prince','Harry Potter and the Deathly Hallows Part-1','Harry Potter and the Deathly Hallows Part-2','The Fast and the Furious','2 Fast 2 Furious','Fast & Furious','Fast Five','Fast & Furious 6','The Fast and the Furious: Tokyo Drift ','Furious 7','The Fate of the Furious','Fast & Furious Presents: Hobbs & Shaw','F9: The Fast Saga','Fast X','Mission: Impossible','Mission: Impossible 2','Mission: Impossible III','Mission: Impossible – Ghost Protocol','Mission: Impossible – Rogue Nation','Mission: Impossible – Fallout','Mission: Impossible – Dead Reckoning Part One', 'Fantastic Beasts and Where to Find Them', 'Fantastic Beasts: The Crimes of Grindelwald', 'Fantastic Beasts: The Secrets of Dumbledore', 
              'The Conjuring','Annabelle','The Conjuring 2','Annabelle: Creation','The Nun','The Curse of La Llorona','Annabelle Comes Home','The Conjuring: The Devil Made Me Do It','Frozen','Frozen 2','Tangled','Zootopia','Moana','Brave','Dumbo','Bambi','Cinderella','Sleeping Beauty'],

    'Genre': ['Fantasy', 'Fantasy','Fantasy', 'Fantasy', 'Fantasy','Fantasy','Fantasy','Fantasy','Action','Action','Action', 'Action', 'Action', 'Action','Action','Action','Action','Action','Action','Action','Action','Action','Action','Action','Action','Action','Fantasy','Fantasy','Fantasy', 'Horror', 'Horror','Horror','Horror','Horror','Horror','Horror', 'Horror', 'Animation', 'Animation', 'Animation', 'Animation', 'Animation','Animation','Animation','Animation','Animation','Animation']
}

movies_df = pd.DataFrame(movies_data)

# User input: Choose a movie from the dataset
user_input_movie = input("Enter the title of a movie from the dataset: ")

# Filter the dataset to include only the selected movie
user_movie = movies_df[movies_df['Title'] == user_input_movie]

if user_movie.empty:
    print(f"Movie '{user_input_movie}' not found in the dataset.")
else:
    # Filter recommendations based on the selected movie's genre
    genre_filter = user_movie['Genre'].values[0]
    recommendations = movies_df[movies_df['Genre'] == genre_filter]

    # Exclude the user's top pick (it's the same as the input)
    recommendations = recommendations[recommendations['Title'] != user_input_movie]

    print(f"Recommendations based on {user_input_movie}:\n")
    print(recommendations[['Title', 'Genre']])
