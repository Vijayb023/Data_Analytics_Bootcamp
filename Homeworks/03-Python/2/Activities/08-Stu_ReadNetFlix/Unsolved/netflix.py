import os 
import csv 

video = input("what video are you looking for")

csvpath = os.path.join("..", "Resources", "Netflix_ratings.csv")
found = False 
with open(csvpath, newline=" ") as csvfile:
    cvsreader = csv.reader(csvfile, delimeter=",")
    for row in cvsreader: 
        if row[0] == video:
        print(row[0] +" is rated with "+ row[5])
        found = True 
        break 
        if found is False:
            print("sorry cant find it")
