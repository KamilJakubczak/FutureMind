from PIL import Image
import io


def generate_dummy_image(filename: str, extension: str) -> io.BytesIO:
    img = Image.new('RGB', (29, 323))
    # img.format = extension
    img.putdata([1, 2])
    im = img
    # im_resize = im.resize((500, 500))
    buf = io.BytesIO()
    img.save(buf, format='JPEG')
    buf.seek(0)
    buf.name = f'{filename}.{extension}'
    return buf


def resize_image(image: object, width: int, height: int) -> io.BytesIO:
    img = Image.open(image)
    resized_img = img.resize((width, height))
    image_buffer = io.BytesIO()
    resized_img.save(image_buffer, format=image.file.image.format)
    image_buffer.seek(0)
    image_buffer.name = image.file.name
    return image_buffer
