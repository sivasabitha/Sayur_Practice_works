'''
2. Define a class for YouTube video. 
decide the properties and functions based on the questions below.

List all the videos recorded by author "Kannan"
List all the videos with more than 1K views
Change the author of all the videos recorded by "Kannan" to "Kannan D."
20 students watched Kannan's "Intro to Python" video today. Update the videos views and print
the total views for this video.
'''
# create a class for youtube videos
class youtubevideo:
    def __init__(self,title,author,views):
        self.title=title
        self.author=author
        self.views=views

# create a empty list to store the details of class youtube video
videos=[]

# initialize the parameters values
v1=youtubevideo("intro to python","kanan",4000)
v2=youtubevideo("intro to java","kanan",5000)
v3=youtubevideo("intro to c","raja",7000)
v4=youtubevideo("intro to c++","rani",9000)
v5=youtubevideo("intro to devops","kanan",10000)
v6=youtubevideo("intro to database","ram",300)
v7=youtubevideo("intro to python","raja",2000)

# append the values in videos list
videos.append(v1)
videos.append(v2)
videos.append(v3)
videos.append(v4)
videos.append(v5)
videos.append(v6)
videos.append(v7)

# List all the videos recorded by author "Kannan"
print("videos recorded by author Kannan : ")
for video in videos:
    if video.author=="kanan":
        print(f"* {video.title}")

#List all the videos with more than 1K views
print("List all the videos with more than 1K views : ")
for video in videos:
    if video.views > 1000:
        print(f"* {video.title}")

#Change the author of all the videos recorded by "Kannan" to "Kannan D."
print("Change the author of all the videos recorded by Kannan to Kannan D.")
for video in videos:
    if video in videos:
        if video.author=="kanan":
            video.author="kanan D."
        print(f"* {video.title},{video.author}")

# 20 students watched Kannan's "Intro to Python" video today. Update the videos views and print
# the total views for this video.
print("update the videos views : ")
for video in videos:
    if video.title=="intro to python" and video.author=="kanan D.":
        video.views += 20
        print(f"* {video.title},{video.author},{video.views}")

'''
OUTPUT:

videos recorded by author Kannan : 
* intro to python
* intro to java
* intro to devops
List all the videos with more than 1K views : 
* intro to python
* intro to java
* intro to c
* intro to c++
* intro to devops
* intro to python
Change the author of all the videos recorded by Kannan to Kannan D.
* intro to python,kanan D.
* intro to java,kanan D.
* intro to c,raja
* intro to c++,rani
* intro to devops,kanan D.
* intro to database,ram
* intro to python,raja
update the videos views :
* intro to python,kanan D.,4020
'''