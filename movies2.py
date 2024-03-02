'''
Problem #4
You are inviting 3 of your friends over to your house for watching a movie.
You have a list of 5 movies you like. Ask each of your friends 5 movies they like.

1. List all the movies everyone likes
2. List only the movies you like but no one else likes
3. List the movies you like and at least one friend likes. Find which friend it is.
4. List the movies all your friends like but you don't like.
'''
# initialize list of your favorite movies
your_favorite_movies = ["A", "B", "C", "D", "E"]

# get your friends favorite movies 
#get the no.of friends and create a empty list to store friends_favorite_movies
no_of_friends = int(input("enter the number of friends: "))
friends_favorite_movies = []
#get the each friends favorite movies and append the movies in friends_favorite_movies list
for i in range(no_of_friends):
    friend_favorite_movies = input(f"enter the friend {i + 1}'s favorite 5 movies separated by commas: ").split(",")
    friends_favorite_movies.append(friend_favorite_movies)

#list of movies everyone likes
#intersection function is help to get a similar movies from your favorite movies to friends favorite movies
movies_everyone_likes = list(set(your_favorite_movies).intersection(*friends_favorite_movies))
print(f"movies everyone likes: {movies_everyone_likes}")

# movies you like and at least one friend likes, along with the friend
#create a empty list for at least one friend likes
movies_atleastone_friend_likes = []
for movie in your_favorite_movies:
    #enumerate function use to iterate the index and index value
    for index, friend_movies in enumerate(friends_favorite_movies,1):
        if movie in friend_movies:
            #inthis list we append the movies and friend who like tht movie
            movies_atleastone_friend_likes.append((movie, f"Friend {index}"))
#print the list you like and at least one friend likes, along with the friend
print(f"movies you like and at least one friend likes:{movies_atleastone_friend_likes}")

# movies all friends like but you don't like
movies_all_friends_like_but_you_dont = list(set.intersection(*map(set, friends_favorite_movies)) - set(your_favorite_movies))
print("movies all your friends like but you don't like:", movies_all_friends_like_but_you_dont)

'''
output:

enter the number of friends: 3
enter the friend 1's favorite 5 movies separated by commas: A,B,E,P,S
enter the friend 2's favorite 5 movies separated by commas: P,S,D,C,A
enter the friend 3's favorite 5 movies separated by commas: C,B,P,S,A
movies everyone likes: ['A']
movies you like and at least one friend likes:[('A', 'Friend 1'), ('A', 'Friend 2'), ('A', 'Friend 3'), ('B', 'Friend 1'), ('B', 'Friend 3'), ('C', 'Friend 2'), ('C', 'Friend 3'), ('D', 'Friend 2'), ('E', 'Friend 1')]
movies all your friends like but you don't like: ['P', 'S']
'''