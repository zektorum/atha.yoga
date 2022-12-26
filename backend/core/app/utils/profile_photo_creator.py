from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings
import os

from PIL import Image
from PIL.ImageDraw import ImageDraw
import uuid


class ProfilePhotoCreator:
    SIZE = 165

    def __init__(self, photo: InMemoryUploadedFile):
        self.photo = photo

    def create(self) -> str:
        profile_photos_dir = os.path.join(settings.MEDIA_ROOT, "user_profile_photos")
        if not os.path.exists(profile_photos_dir):
            os.makedirs(profile_photos_dir)
        profile_photo_path = os.path.join(profile_photos_dir, f"{uuid.uuid4()}.png")
        profile_photo = self._create_profile_photo_from_file(self.photo)
        profile_photo.save(fp=profile_photo_path)
        return profile_photo_path

    def _create_profile_photo_from_file(self, file: Image) -> Image:
        image = Image.open(file)
        width, height = image.size
        if width != height:
            image = self._make_square(image)
        image.thumbnail(size=(self.SIZE, self.SIZE))
        image.putalpha(self._make_circle_mask(self.SIZE))
        return image

    def _make_square(self, image: Image) -> Image:
        width, height = image.size
        if height < width:
            square = image.crop(
                ((width - height) // 2, 0, (width - height) // 2 + height, height)
            )
        else:
            square = image.crop((0, 0, width, width))
        return square

    def _make_circle_mask(self, radius: int) -> Image:
        mask = Image.new("L", (radius, radius))
        mask_draw = ImageDraw(mask)
        mask_draw.ellipse((0, 0, radius, radius), fill=255)
        return mask
