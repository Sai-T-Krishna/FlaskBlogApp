#### Blogproject/users/picture_handler.py
#### we will use PIL  or pillow library

import os
from PIL import Image
from flask import url_for, current_app

#adding profile pic
def add_profile_pic(pic_upload, username):
    
    filename = pic_upload.filename
    ## "mypicture . "jpg"
    ext_type = filename.split('.')[-1]
    ## when someone uploads a picture we will save it as "username.jpg"
    storage_filename = str(username) + '.' + ext_type
    file_path = os.path.join(current_app.root_path,'static/profile_pics',storage_filename)

    output_size = (200, 200)

    pic = Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(file_path)

    return storage_filename