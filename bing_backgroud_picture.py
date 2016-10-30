import requests
import os

BASE_DIR = 'E:\\bing_back_ground'
api_url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

resp_json = requests.get(api_url).json()

copyright = resp_json['images'][0]['copyright']
date = resp_json['images'][0]['enddate']
image_url = resp_json['images'][0]['url']

# print copyright, date, image_url
Image_dir = os.path.join(BASE_DIR, date)
if not os.path.exists(Image_dir):
    os.mkdir(Image_dir)
image_name = image_url.split('/')[-1]
image_path = os.path.join(Image_dir, image_name)
# print image_path
image_byte = requests.get(image_url).content
if not os.path.exists(image_path):
    with open(image_path, 'wb') as image:
        image.write(image_byte)
