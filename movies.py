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
    # __init__ object creation, constructor --> creating the object 
    def __init__(self,name,location,owner_name,no_of_seats):
        #we define a entity or properties
        #self indictes current objact
        self.name=name
        self.current_movie=""
        self.location=location
        self.owner_name=owner_name
        self.no_of_seats=no_of_seats
    # __str__ useto represent human readable format
    def __str__(self):
        return self.name+" "+self.location
    
    # def __repr__(self):
    #     return self.name+" "+self.location
# collection of movie_theatre objects
theatres=[]
theatre_dict={}

inox=movie_theatre("inox","madurai","vijay",200)
inox_covai=movie_theatre("inox","covai","vijay",200)
vetri=movie_theatre("vetri","madurai","jay",400)
vetri_chenni=movie_theatre("vetri","chennai","jay",400)
varatharaja=movie_theatre("varatharaja","chennai","raja",400)
gopuram=movie_theatre("gopuram","madurai","ram",300)
inox_chennai=movie_theatre("inox","chennai","sivasabitha",100)

theatres.append(inox_covai)
theatres.append(vetri_chenni)
theatres.append(inox)
theatres.append(vetri)
theatres.append(varatharaja)
theatres.append(gopuram)
theatres.append(inox_chennai)

'''
ex:dict objects must have unique keys. In an expression like D = {'a':1,'a':2}, the dict is constructed 
taking the last key-value pair with the non-unique key, from left to right.
so it will simply evaluate to {'a':2}
'''

for theatre in theatres:
    # setdefault --> It returns the value of the item with the specified key
                # setdefault[keyname,value]
    theatre_dict.setdefault(theatre.name,[]).append(theatre.location)
print(theatre_dict)

print("Theatre placed in more than one places: ")
for theatre.name,theatre.location in theatre_dict.items():
    if len(theatre.location)>1:
        print(f"Theatre name: {theatre.name},Locations: {theatre_dict[theatre.name]}")    

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

{'inox': ['covai', 'madurai', 'chennai'], 'vetri': ['chennai', 'madurai'], 'varatharaja': ['chennai'], 'gopuram': ['madurai']}
Theatre placed in more than one places:
Theatre name: inox,Locations: ['covai', 'madurai', 'chennai']
Theatre name: vetri,Locations: ['chennai', 'madurai']
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
