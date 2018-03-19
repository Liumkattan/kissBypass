from django.contrib.postgres.fields import JSONField
from django.db import models
# import json


class Imagehashes(models.Model):
    image_hash = models.CharField(max_length=16)
    image_words = JSONField()

    def __str__(self):
        return self.image_hash

    # def set_words(self, x):
    #     self.image_words = json.dumps(x)

    # def get_words(self):
    #     return json.loads(self.image_words)
