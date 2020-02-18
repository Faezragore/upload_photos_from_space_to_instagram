import os
import pathlib
import argparse
import requests


def get_links_to_the_first_image_in_the_Hubble_API(url):
    links = []
    response = requests.get(url, verify=False)
    links_to_images = response.json()["image_files"]

    for link in links_to_images:
        links.append('http:' + link["file_url"])
    return links


def download_picture_from_Hubble(id_image):
    path = os.getcwd()
    pathlib.Path('%s/images' % (path)).mkdir(parents=True, exist_ok=True)

    links = get_links_to_the_first_image_in_the_Hubble_API(
            'http://hubblesite.org/api/v3/image/%s' % (id_image))
    url = links[-1]
    response = requests.get(url, verify=False)

    with open('%s/images/%s.%s' % (
              path, id_image, os.path.splitext(url)[1]), 'wb') as file:
        file.write(response.content)


def download_the_collection_of_pictures_API_hubble():
    url = 'http://hubblesite.org/api/v3/images/%s?page=all' % (
          name_of_collection)
    response = requests.get(url, verify=False)
    id_images = response.json()

    for id_image in id_images:
        download_picture_from_Hubble(id_image["id"])


def main():
    parser = argparse.ArgumentParser(description='enter a collection name')
    parser.add_argument('the_name_of_the_collection', help='collection name')
    args = parser.parse_args()
    the_name_of_the_collection = args.the_name_of_the_collection

    download_the_collection_of_pictures_API_hubble(the_name_of_the_collection)


if __name__ == '__main__':
    main()
