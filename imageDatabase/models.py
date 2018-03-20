from django.db import models


class Imagehashes(models.Model):
    image_hash = models.CharField(max_length=16)
    image_words = models.CharField(max_length=300, default=str)

    def __str__(self):
        return self.image_hash

    def set_words(self, word):
        self.image_words += ";" + str(word)

    def get_words(self):
        return self.image_words.split(";")
