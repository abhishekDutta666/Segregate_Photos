'''
The package structure should be 
users
    -user1
        -photo1.jpg
        -photo2.jpg
    -user2
        .
        .
        .

'''
import os
from deepface import DeepFace
import pandas as pd

if __name__=="__main__": 
    os.chdir('..')
    CWD=os.getcwd()
    DB_DIR=os.path.join(CWD, 'photos_database')
    USERS_DIR=os.path.join(CWD, 'users')
    for user in os.listdir(USERS_DIR):  
        df = DeepFace.find(img_path=os.path.join(USERS_DIR, user), db_path=DB_DIR)
        print("USER: ", os.path.basename(user))
        for index, row in df.iterrows(): 
            print (row["identity"], row["VGG-Face_cosine"]) 