import time
import os
import praw
import shutil
# Imports nessesary Moduel for program
from cred import cred
# Imports Credintals for Haptic bot (Praw)

imgur_use = 0
redgif_use = 0
x = 0
#Sets Up variables for later in program

os.system("clear")

subrd = input ("What subreddit would you like to browse today?: ")
att = input ('How many inputs do you want?: ')

lim = str("limit =" + str(att))

#Coustomizing the rules for the bot

while x < 1:
# while variable is less than the number of posts you want
    subreddit = cred.subreddit(subrd).hot(limit = int(att))
# go to reddit and request content
    for submission in subreddit:
    #for each content request do this

        print("Title: " + str(submission.title))
        print("SubmissionId" + submission.id)
        url = str(submission.url)
        id = str(submission.id)
        if len(str(submission.title)) >= 30:
            title = str(submission.title[0:30])
        else:
            title = str(submission.title)
            
        if url.endswith(".jpg"):
            if os.path.isfile("pic_gif_output/Pictures/" + id + ".jpg"):
                print ("File is already downloaded moving to next file")
            else:
                os.system("wget -qO" + " pic_gif_output/Pictures/" + id + ".jpg" + " " + url)
        # sorts .jpg's
        elif url.endswith(".png"):
            if os.path.isfile("pic_gif_output/Pictures/" + id + ".png"):
                print ("File is already downloaded moving to next file")
            else:
                os.system("wget -qO" + " pic_gif_output/Pictures/" + id + ".png" + " " + url)
        #sorts .png's
        elif url.endswith(".gifv"):
            imgur_use += 1
            if os.path.isfile("pic_gif_output/Gifs/" + id + ".mp4"):
                print ("File is already downloaded moving to next file")
            else:
                os.system("gallery-dl " + url)
        # sorts .gifv's
        elif url.startswith("https://redgifs.com"):
            redgif_use += 1
            if os.path.isfile("pic_gif_output/Gifs/" + id + ".mp4"):
                print ("File is already downloaded moving to next file")
            else:
                os.system("gallery-dl " + url)
        #sorts anything posted from redgif
        else:
            file = open(str("pic_gif_output/Texts/" + title + ".txt"), 'x')
            file.write(submission.selftext)
            file.close()
        #puts anything else into a text formatted file
    x += 1
    time.sleep(1)
    #tells the program how many times its run this code to break loop and then sleep for one sec (DONE FOR LOW RAM DEVICES)
    
if redgif_use != 0:
    old_directory = "gallery-dl/redgifs/"
    new_directory = "pic_gif_output/Gifs/"
    for filename in os.listdir(old_directory):
        if filename.endswith(".mp4"):
            source = os.path.join(old_directory, filename)
            destination = os.path.join(new_directory, filename)
            dest = shutil.copyfile(source, destination)
#puts files in there correct place both for redgif and imgur

if imgur_use != 0:
    old_directory = "gallery-dl/imgur"
    new_directory = "pic_gif_output/Gifs"
    for filename in os.listdir(old_directory):
        if filename.endswith(".mp4"):
            source = os.path.join(old_directory, filename)
            destination = os.path.join(new_directory, filename)
            dest = shutil.copyfile(source, destination)

if imgur_use or redgif_use != 0:
    os.system('rm -rdf gallery-dl/')
#deletes the gallery-dl file created from a file downloader called "gallery-dl"
