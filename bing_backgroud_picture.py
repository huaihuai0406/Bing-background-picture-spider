import requests
import os
import time
import sys

from qiniu import Auth, put_data, etag, urlsafe_base64_encode
import qiniu.config


BASE_DIR = 'E:\\bing_back_ground'
api_url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

resp_json = requests.get(api_url).json()

icopyright = resp_json['images'][0]['copyright']
date = resp_json['images'][0]['enddate']
image_url = resp_json['images'][0]['url']
image_name = image_url.split('/')[-1]
image_byte = requests.get(image_url).content


def save_local(data, base_path, date = time.time()):
    image_dir = os.path.join(base_path, date)
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)

    # image_name = image_url.split('/')[-1]
    image_path = os.path.join(image_dir, image_name)

    with open(image_path, 'wb') as f:
        f.write(data)


def save_qiniu(data, image_name):
    assess_key = os.environ.get('QINIUAK')
    secret_key = os.environ.get('QINIUSK')

    q = Auth(assess_key, secret_key)

    bucket_name = 'bing-background-picture'
    key = os.path.join(os.sep, date, image_name)
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_data(token, key, data)
    print info


if __name__ == '__main__':
    if sys.platform == 'win32':
        save_local(image_byte, BASE_DIR, date)
    elif sys.platform == 'linux2':
        save_qiniu(image_byte, image_name)