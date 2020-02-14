import os
import requests
import pathlib


def function_to_download_pictures(url, filename):
    print(os.getcwd())
    path = os.getcwd()
    pathlib.Path('%s/images' % (path)).mkdir(parents=True, exist_ok=True)
    response = requests.get(url, verify=False)

    with open('%s/images/%s' % (path, filename), 'wb') as file:
        file.write(response.content)


def get_photos_from_SpaceX_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url, verify=False)
    number_index = response.json()["links"]["flickr_images"]
    return number_index


def fetch_spacex_last_launch():
    links_to_the_picture = get_photos_from_SpaceX_launch()
    for name, url in enumerate(links_to_the_picture):
        filename = 'spacex%d.jpg' % (name)
        function_to_download_pictures(url, filename)

        
def main():
    fetch_spacex_last_launch()


if __name__ == '__main__':
    main()
