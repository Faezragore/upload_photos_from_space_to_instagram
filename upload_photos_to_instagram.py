import os
from os import listdir
from os.path import isfile
from os.path import join as joinpath
import time
import argparse
from dotenv import load_dotenv
from PIL import Image
from instabot import Bot
load_dotenv()


def instabot(your_login, your_password, the_path_to_the_folder):
    bot = Bot()
    bot.login(username=your_login, password=your_password)
    for photo_name_and_extension in listdir(the_path_to_the_folder):
        timeout = 60
        time.sleep(timeout)
        if isfile(joinpath(the_path_to_the_folder, photo_name_and_extension)):
            bot.upload_photo("%s/%s" % (the_path_to_the_folder, photo_name_and_extension), caption="Super Typhoon Maysak ")


def main():
    your_login = os.getenv("LOGIN")
    your_password = os.getenv("LOGIN_PASSWORD")
    parser = argparse.ArgumentParser(description='Specify the path to the folder where the photos are located')
    parser.add_argument('path', help='your way to the folder')
    args = parser.parse_args()
    the_path_to_the_folder = args.path
    instabot(your_login, your_password, the_path_to_the_folder)


if __name__ == '__main__':
    main()
