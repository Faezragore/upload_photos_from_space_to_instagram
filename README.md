# upload_photos_from_space_to_instagram

### project objective: 
 #### download photos on the theme of space.
 *   photo SpaceX rocket launch(Elon Musk's Company).
 *   beautiful images of space from [Hubble Telescope](https://hubblesite.org). 
 *   upload them to your account [instagram](https://www.instagram.com).

### Installation:

Python3 should be already installed. 
Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```
### Setup:
To upload to instagram, you need an account and a token.
* get an instagram account: register in https://www.instagram.com
  have an account?  let's move on to the item: getting a token
* This is how to get an Instagram API access token: https://docs.oceanwp.org/article/487-how-to-get-instagram-access-token 

 Create a file in the repository __.env__ and substitute the data in the file.
 Sample file __.env__
```
 TOKEN=your token
 YOUR_LOGIN=your login
 YOUR_PASSWORD=your password
```

## Launch: 
   Work is done on the command line.
   There are 3 scripts in the repository.
   > fetch_spacex_last_launch.py: downloads photos from Last SpaceX rocket launch.
   
        To run:  In command line: ``` python fetch_spacex_last_launch.py 'Specify the path to the folder where the photos will be downloaded' ``` 
   > fetch_hubble.py: downloads photos from the Hubble Telescope collection.
        To run:  In command line: ```python fetch_hubble.py 'enter a collection name' ```
        the name of the collections: "holiday_cards", "wallpaper", "spacecraft", "news", "printshop", "stsci_gallery".
   > upload_photos_to_instagram.py: uploads photos to instagram.
   


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
