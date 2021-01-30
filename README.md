# Segregate_Photos

## What does this do ?

Given a one reference picture for each user and a database of pictures, this program segregates all the images in folders depending which user was in which picture.
What this means is that if in Img1.jpg, userA and userB are present, Img1.jpg will be copied into folders userA and userB.

### Why did I make this ?

After every outing, my friends and family usually ask me to send all the pictures in which they are present. This becomes quite an hassle if the number of people crosses 2. So I built
this program utilize the power of AI to make my life a little easier.

### How to install

```python
pip install -r requirements.txt
```

In case you are using windows, install visual studio 2019 with windows 10 SDK. This has to be done as face_recognition package is not natively supported on windows.

### How to use

- Put this folder where you want to segregate the pictures
- put all the pictures that need to be segregated in a folder called 'photos_database'
- Put all the individual photos that have to be used as reference in a folder called 'users'
- The name of these individual images will be used as the name of the segregated folders, hence name them accordingly
- Follow the installation procedure
- Run python3 usingFaceRecognizer.py or python3 usingDeepFace.py
