'''
OOP problem.
1. Define a class for movie theatre. 
Properties should be Name, current movie, Location, and Owner name.
All fields except Current movie should have value.
Add a constructor to create a new theatre.
Add functions to change the current movie.

In the program, create 5 movie theatres.
List all the theatres in Madurai
List all the theatres that is running the movie "Captain America"
'''
class movie_theatre:
    def __init__(self,name,location,owner_name):
        #we define a entity
        #self indictes current objact
        self.name=name
        self.current_movie=""
        self.location=location
        self.owner_name=owner_name

    def __str__(self):
        return self.name+" "+self.location
    
    # def __repr__(self):
    #     return self.name+" "+self.location

theatres=[]


inox=movie_theatre("inox","madurai","vijay")
vetri=movie_theatre("vetri","madurai","jay")
varatharaja=movie_theatre("varatharaja","chennai","raja")
gopuram=movie_theatre("gopuram","madurai","ram")
theatres.append(inox)
theatres.append(vetri)
theatres.append(varatharaja)
theatres.append(gopuram)

inox.current_movie="capton america"
vetri.current_movie="ayalaan"
varatharaja.current_movie="vikram"
gopuram.current_movie="capton america"
# print(theatres[1])

print("movie theatres in madurai : ")
for theatre in theatres:
    if theatre.location == "madurai":
        print("theatre location : ",theatre.name)

print("capton america movie running places : ")
for theatre in theatres:
    if theatre.current_movie == "capton america":
        print("theatre name : ", theatre.name)
    
inox.current_movie="ayalaan"
print("capton america movie running places : ")
for theatre in theatres:
    if theatre.current_movie == "capton america":
        print("theatre name : ", theatre.name)

'''
OUTPUT:

movie theatres in madurai : 
theatre location :  inox
theatre location :  vetri
theatre location :  gopuram
capton america movie running places : 
theatre name :  inox
theatre name :  gopuram
capton america movie running places :
theatre name :  gopuram

'''
