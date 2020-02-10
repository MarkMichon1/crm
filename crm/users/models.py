from django.contrib.auth.models import User
from django.db import models
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.image.path)
        if image.height > 250 or image.width > 250:
            output_size = (250, 250)
            image.thumbnail(output_size)
            image.save(self.image.path)