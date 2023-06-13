from pprint import pprint

import requests
import json
from zipfile import ZipFile
import os

dir_for_zip = 'D:\PycharmProjects\Python-Core\Virus_check\Test_dir'

def get_link(api_key='bc23fdddeb3bdeaeea3bd4091c1bfd61f08659909b523b4f6cc14ad2eeff5772'):
    url = "https://www.virustotal.com/api/v3/files/upload_url"
    headers = {
        "accept": "application/json",
        "x-apikey": api_key
    }
    response = requests.get(url, headers=headers)
    print('Ссылка для отправки получена: ',response.text)
    return response.text


def zip_file(dir_for_zip):

    if not os.path.exists('for_upload.zip'):
        z = ZipFile('for_upload.zip','w')
        for root,dirs,files in os.walk(dir_for_zip):
            for file in files:
                z.write(os.path.join(root,file))
        z.close()
        print('Запаковано в ',os.path.basename("for_upload.zip"),end='')
        print(os.path.getsize(os.path.basename("for_upload.zip")))
    else:
        print(f'Файл \"{os.path.basename("for_upload.zip")}\",{os.path.getsize(os.path.basename("for_upload.zip"))/1024.0*1024.0} уже существует')

# zip_file(dir_for_zip)

def upload(api_key):
    url = "https://www.virustotal.com/api/v3/files"

    files = {"file": ("for_upload.zip", open("for_upload.zip", "rb"), "application/zip")}
    headers = {
        "accept": "application/json",
        "x-apikey": "bc23fdddeb3bdeaeea3bd4091c1bfd61f08659909b523b4f6cc14ad2eeff5772"
    }

    response = requests.post(url, files=files, headers=headers)

    print(response.text)


# upload(api_key='bc23fdddeb3bdeaeea3bd4091c1bfd61f08659909b523b4f6cc14ad2eeff5772')

def req():
    url = "https://www.virustotal.com/api/v3/files/ZjE3MDRlZjUxZWU4OTc5ZjBiNGZjOWFlOTQ4MGY1MDk6MTY3ODc4NzU5OQ%3D%3D"
    headers = {
        "accept": "application/json",
        "x-apikey": "bc23fdddeb3bdeaeea3bd4091c1bfd61f08659909b523b4f6cc14ad2eeff5772"
    }
    response = requests.get(url, headers=headers)
    print(response.text)
# req()




with open('D:\PycharmProjects\Python-Core\Virus_check\scan_req.json','rb') as file:
    r = json.load(file)
pprint(r['data']['links']['self'])
pprint(r['data']['links']['self'])
