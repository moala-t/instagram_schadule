# set environment
import os
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'instagram_schadule.settings'
django.setup()

from instagrapi import Client
from time import sleep
import pathlib
from content.models import Content
from datetime import datetime
from extensions import video_extensions
from django.utils import timezone


# --------------- FUNCTIONS ---------------
def is_video(path:str):
    extension = path.strip().split(".")[-1]
    for i in video_extensions:
        if i == extension:
            return True
    return False

def create_path(path):
    return pathlib.Path(__file__).parent.joinpath(path)

def uplaod_content(content:Content):
    file_path = create_path(str(content.file))
    
    if is_video(str(file_path)):
        if content.is_post: 
            client.video_upload(file_path, content.caption)
        elif content.is_story:
            client.video_upload_to_story(file_path)
    else:
        if content.is_post:
            client.photo_upload(file_path, content.caption)
        elif content.is_story:
            client.photo_upload_to_story(file_path)

# --------------- MAIN ---------------
client = Client()
# client.set_proxy('http://127.0.0.1:10809')
client.login("sahabahq", "Sq@1695987")

while True:
    for content in Content.objects.all():
        if datetime.timestamp(content.schadule) <= datetime.timestamp(timezone.now()):
            uplaod_content(content)
            print(f"{timezone.now()} ~> '{content.name}' UPLOADED TO INSTAGRAM")
            sleep(10)
            content.delete_with_file()
    sleep(60)
    