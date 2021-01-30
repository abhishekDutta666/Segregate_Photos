'''
The package structure should be 
-SegregatePhotos
-users
    -user1.jpg
    -user2.jpg
        .
        .
        .
-photos_database
    -photo1.jpg
    -photo2.jpg
    -photo3.jpg
        .
        .
        .
'''
import os
import face_recognition
import datetime
import shutil

if __name__=="__main__": 
    os.chdir('..')
    CWD=os.getcwd()
    DB_DIR=os.path.join(CWD, 'photos_database')
    USERS_DIR=os.path.join(CWD, 'users')
    date = datetime.date.today()
    SEGREGATED_DIR=os.path.join(CWD, 'Segregated_Output')
    os.mkdir(SEGREGATED_DIR)
    names=[]
    encodings=[]
    for user in os.listdir(USERS_DIR):  
        user_img=face_recognition.load_image_file(os.path.join(USERS_DIR, user))
        encodings.append(face_recognition.face_encodings(user_img)[0])
        IMG_FILE_NAME=user[0:-4]+' '+str(date)
        USER_IMG_LOC=os.path.join(SEGREGATED_DIR, IMG_FILE_NAME)
        names.append([IMG_FILE_NAME, USER_IMG_LOC])
        os.mkdir(USER_IMG_LOC)
    for image in os.listdir(DB_DIR):
        img_loc=os.path.join(DB_DIR, image)
        unknown_image=face_recognition.load_image_file(img_loc)
        all_faces_in_unknown_image=face_recognition.face_encodings(unknown_image)
        for unknown_face_encoding in all_faces_in_unknown_image: 
            results = face_recognition.compare_faces(encodings, unknown_face_encoding)
            for i in range(len(results)):
                if results[i]:
                    print(image," added to ",names[i][0], " folder")
                    shutil.copy2(img_loc, names[i][1])
    print("the program has finished processing")



                    

