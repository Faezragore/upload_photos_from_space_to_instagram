import os
import pathlib
import argparse
import requests

def output_links_to_the_first_image_in_the_Hubble_API(url):
    list_of_links = []
    response = requests.get(url, verify=False)
    number_index = response.text
    number_index = number_index[number_index.find('image_files') + 14:-2].split('"')
    for i in number_index:
        if '//' in i:
            list_of_links.append('http:'+i)
    return list_of_links

def to_show_the_extension_of_the_image(url):
    return url.split('.')[-1]

def download_pictures_from_Hubble(id_image):
    path = os.getcwd()
    pathlib.Path('%s/images' % (path)).mkdir(parents=True, exist_ok=True)

    list_of_links = output_links_to_the_first_image_in_the_Hubble_API('http://hubblesite.org/api/v3/image/%s' % (id_image))
    url = list_of_links[-1]
    response = requests.get(url, verify=False)

    with open('%s/images/%s.%s' % (path,id_image,to_show_the_extension_of_the_image(list_of_links[-1])), 'wb') as file:
        file.write(response.content)

def download_the_collection_of_pictures_API_hubble(the_name_of_the_collection):
    url = 'http://hubblesite.org/api/v3/images/%s?page=all' % (the_name_of_the_collection)
    response = requests.get(url, verify=False)
    list_id_images = response.text.split(',')

    for id_images in list_id_images:
        if '{"id":' in id_images:
            download_pictures_from_Hubble(id_images.split(':')[1])

def main():
    parser = argparse.ArgumentParser(description='enter a collection name')
    parser.add_argument('the_name_of_the_collection', help='collection name')
    args = parser.parse_args()
    the_name_of_the_collection = args.the_name_of_the_collection

    download_the_collection_of_pictures_API_hubble(the_name_of_the_collection)


if __name__ == '__main__':
    main()
