import os
from uuid import uuid4


def customer_image_name(instance, filename: str):
    """Generate file path for new image"""
    ext = filename.split('.')[-1]
    filename = f'{str(uuid4())[:10]}.{ext}'
    return os.path.join('images/', filename)


