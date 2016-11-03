from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import os

assess_key = os.environ.get('QINIUAK')
secret_key = os.environ.get('QINIUSK')

q = Auth(assess_key, secret_key)

bucket_name = 'bing-background-picture'

key = 'temp.jpg'
token = q.upload_token(bucket_name, key, 3600)

localfile = 'E:\\temp.jpg'
ret, info = put_file(token, key, localfile)
print ret, info
assert ret['key'] == key
assert ret['hash'] == etag(localfile)
