import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath
import time
import argparse

from dotenv import load_dotenv
load_dotenv()
from PIL import Image
from instabot import Bot

def list_of_files_in_a_folder(the_path_to_the_folder):   
    mypath = "%s" % (the_path_to_the_folder)
    for photo_name_and_extension in listdir(mypath):
        if isfile(joinpath(mypath,photo_name_and_extension)):
            find_out_the_size_of_the_picture(the_path_to_the_folder,photo_name_and_extension)
         
def find_out_the_size_of_the_picture(the_path_to_the_folder,photo_name_and_extension):
    image = Image.open("%s/%s" % (the_path_to_the_folder,photo_name_and_extension))
    if max(image.size) == image.size[0]:
        picture_cropping_length =(int((max(image.size) - min(image.size))/2))
        coordinates = (picture_cropping_length, 0, image.width - picture_cropping_length, image.height)
        cropped = image.crop(coordinates)
        cropped.save("%s/pize/%s" % (the_path_to_the_folder,photo_name_and_extension))
    elif max(image.size) == image.size[1]:
        picture_cropping_length =(int((max(image.size) - min(image.size))/2))
        coordinates = (0, picture_cropping_length, image.width, image.height - picture_cropping_length)
        cropped = image.crop(coordinates)
        cropped.save("%s/pize/%s" % (the_path_to_the_folder,photo_name_and_extension))
    else:
        print("circumcision is not required")

def instabot(your_login,your_password,the_path_to_the_folder):
    bot = Bot()
    bot.login(username=your_login, password=your_password)
    for photo_name_and_extension in listdir(the_path_to_the_folder):
        timeout = 60
        time.sleep(timeout)
        if isfile(joinpath(the_path_to_the_folder,photo_name_and_extension)):
            bot.upload_photo("%s/%s" % (the_path_to_the_folder,photo_name_and_extension), caption="Super Typhoon Maysak ")

def main():
    your_login = os.getenv("LOGIN")
    your_password = os.getenv("LOGIN_PASSWORD")
    parser = argparse.ArgumentParser(description='Specify the path to the folder where the photos will be downloaded')
    parser.add_argument('path', help='your way to the folder')
    args = parser.parse_args()
    the_path_to_the_folder = args.path
    instabot(your_login,your_password,the_path_to_the_folder)

if __name__ == '__main__':
    main()
