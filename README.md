# Netflix Data Analysis with Pandas
Hi!!! Welcome to my Netflix pandas project. This project focuses on a dataset I downloaded from Kaggle. Here's the link in case you also want to have fun with it [https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies].

So, I finished the Pandas course on Kaggle and decided to test my skills on a real life dataset and see how well I do. The dataset contains information on TV shows and Movies, actors, the imdb popularity, rating and all that stuff.

This project was inspired by a series of structured challenges where I had to analyze a dataset under the guidance of an unseen but strict 'examiner.' No hints, no shortcuts—just pure problem-solving and data exploration. It was tough, exciting, enlightening and a good experience

This project answers 5 questions:
1. What are the unique roles in 'role'?
2. How many movies vs. TV shows?
3. Who are the most frequent actors?
4. What’s the highest-rated movie?
5. Who is the most popular actor (highest 'tmdb_popularity')?


So here's my full walkthrough:

## Bringing the items to the kitchen
I first imported pandas to my code.

![image](https://github.com/user-attachments/assets/bb12cf9c-9948-4f30-aa06-68f182f6d340)


After that was out of the way, I had Pandas read the datasets, and ofcourse join them. But while opening the datasets on Excel, I noticed that they both had an ID column. That would make reading the dataset easier since they both have IDs. Thus, I added the .set_index() method to the code.

![image](https://github.com/user-attachments/assets/97759dd2-c7c9-424e-8a7b-3c5b9ba0afa8)

Now I could play around with the data. 

## First Question
What are the unique roles in the role column? Now this column has 77801 records. I can not literally scan over 77801 records picking out each unique item. It's not that I'm lazy :sweat_smile:, it's just not effective. That's why I'd use pandas.
I can call the index of the column I want, in this case 'role', and run the method .value_counts() to count the unique values and add them up. I save this to a variable called 'unique_roles'.
Now, I print out the results. If I print out the result of 'unique_roles' directly, I'd get a Series object and not everyone knows how to interprete Pandas results. So, I did some string formatting and this is how it looks:
### Code:

![image](https://github.com/user-attachments/assets/49269ae2-2ffa-4355-8310-a07686891f83)

### Result:

![image](https://github.com/user-attachments/assets/53925182-ed92-4453-96c7-ef2887d9aa0e)

Looks clean now :smirk:

## Second Question
How many movies vs. TV shows? Now this one was easy. I just did what I did in the first question. This time, however, my target column was 'type', because that was the column that had the MOVIE and SHOW records. For the output, I used an f-string since it was just numbers I was to display out to answer the question. I used .iloc[] and the index numbers to produce the results.
### Code:

![image](https://github.com/user-attachments/assets/9c63a136-397f-4b3d-b43e-d848fc51296b)

### Result:

![image](https://github.com/user-attachments/assets/7102471b-2203-4036-bf36-c38dcf7e25cf)

## Halfway Mark :grin:
Who are the most frequent actors? It seemed like I'd just run it straight, then it hit me. The column that contained actors also had directors in it :smiling_face_with_tear:
So, I had to create a DataFrame named actors_only, filtering out the dataset to only contain actors. This is where pandas indexing came into play. The dataset was 'net_joined' with all the information I need. So I called the index of the dataset with the column 'role' and specified that I only want actors. Saved it as 'actors_only'.
Now it was time so see the top dogs in this dataset. Ran the value_counts() to my specialised dataset which I called 'frequent_actors', but this time I indexed it to the 'name' column (frequent_actors['name'].value_counts()).
Printed my result with string formatting and even gave a table showing the hierachy. You're welcome :relieved:
### Code:

![image](https://github.com/user-attachments/assets/a2bb805d-7e8f-4bf5-a75a-167a4cb0b385)

### Output:

![image](https://github.com/user-attachments/assets/1bf7b95b-1515-41ae-bf34-56b43e667f1f)

