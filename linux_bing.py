import requests
import os
import time
import sys

from qiniu import Auth, put_data, etag, urlsafe_base64_encode
import qiniu.config


api_url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1'

resp_json = requests.get(api_url).json()

date = resp_json['images'][0]['enddate']
image_url = resp_json['images'][0]['url']
image_name = image_url.split('/')[-1]
image_byte = requests.get(image_url).content

assess_key = os.environ.get('QINIUAK')
secret_key = os.environ.get('QINIUSK')

q = Auth(assess_key, secret_key)

bucket_name = 'bing-background-picture'
key = image_name
token = q.upload_token(bucket_name, key, 3600)
ret, info = put_data(token, key, image_byte)
print info
