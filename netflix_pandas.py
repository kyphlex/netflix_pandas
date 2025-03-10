#Importing pandas to the code
import pandas as pd

#The extraction of the data and joining both datasets together.
net_credits = pd.read_csv('credits.csv')
net_titles = pd.read_csv('titles.csv')
net_joined = net_credits.set_index('id').join(net_titles.set_index('id'))

#Answer to the first question
print("What are the unique roles in 'role'?")
unique_roles = net_joined['role'].value_counts()
print("The dataset contains two unique roles:", ' and '.join(unique_roles.index.tolist()))

#Answer to the second question
print('\nHow many movies vs. TV shows?')
type_count = net_joined['type'].value_counts()
print(f'There are {type_count.iloc[0]} movies and {type_count.iloc[1]} TV shows.')

#Answer to the third question
print('\nWho are the most frequent actors?')
actors_only = net_joined[net_joined['role']=='ACTOR']
frequent_actors = actors_only['name'].value_counts()
print("The top 5 most frequent actors are:", ', '.join(frequent_actors.index[:5].tolist()))
print(frequent_actors.head())

#Answer to the fourth question
print('\nWhat’s the highest-rated movie?')
movies_only = net_titles[net_titles['type']=='MOVIE']
movies = movies_only.set_index('title')
movies_highest = movies[['tmdb_score', 'imdb_score']].fillna(0).mean(axis=1).sort_values(ascending=False)
print(f'The highest rated movie is {movies_highest.index[0]} with an average rating of {movies_highest.iloc[0]}')

#Answer to the fifth question
print("\nWho is the most popular actor (highest 'tmdb_popularity')?")
popular_actors = actors_only[['name', 'tmdb_popularity']].sort_values(by='tmdb_popularity', ascending=False).fillna(0).drop_duplicates(subset='name')
print(f'The most popular actor is {popular_actors['name'].iloc[0]} with {popular_actors['tmdb_popularity'].iloc[0]} points.')
print('Top ten most popular:', f'\n{popular_actors[:10]}')