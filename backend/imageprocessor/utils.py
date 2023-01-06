from PIL import Image
import io


def generate_dummy_image(filename: str, extension: str) -> io.BytesIO:
    img = Image.new('RGB', (29, 323))
    img.format = extension
    img.putdata([1, 2])
    im = img
    im_resize = im.resize((500, 500))
    buf = io.BytesIO()
    im_resize.save(buf, format='JPEG')
    buf.seek(0)
    buf.name = f'{filename}.{extension}'
    return buf