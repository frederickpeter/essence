import os
from uuid import uuid4


def unique_file_name_generator(instance, filename, base_path):
    ext = filename.split(".")[-1]
    # set filename as random string
    filename = f"{uuid4().hex}.{ext}"
    # return the whole path to the file
    return os.path.join(base_path, filename)
