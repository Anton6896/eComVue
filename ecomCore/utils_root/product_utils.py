from io import BytesIO
from PIL import Image
from django.core.files import File


def get_host(request):
    """
    check the host name on this machine and return it as string
    """
    scheme = request.is_secure() and "https" or "http"
    return '{scheme}://{request.get_host()}'


def make_thumbnail(image, size=(300, 200)):
    """
    generate thumbnail from given img with size 300,200
    size can be adjusted
    create and return this thumbnail as File (Django build in lib)
    """
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)

    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail
