from rest_framework import serializers
from .models import Imagehashes
from django.core.exceptions import MultipleObjectsReturned


class ImageHashSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagehashes
        fields = ('image_hash', 'image_words')


class ImageWordesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagehashes
        fields = ['get_words']


class ImageInputSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagehashes
        fields = ['image_hash', 'image_words']

    def validate(self, value):
        try:
            ihash = None
            exists = False
            try:
                ihash = Imagehashes.objects.get(image_hash=value['image_hash'])
                print(ihash.image_hash, "\n\n\n")
                exists = True
            except Imagehashes.DoesNotExist:
                return value
                pass
            if exists:
                if value['image_words'] not in ihash.image_words:
                    imgHash, created = Imagehashes.objects.update_or_create(image_hash=value['image_hash'],
                                                            defaults={"image_words": ihash.image_words + ";" + value['image_words']})
                    raise Exception("Already Exists, Image words updated")
            raise Exception("Already Exists!!")
        except MultipleObjectsReturned:
            raise MultipleObjectsReturned("There is more than one value")
        return value


class HashSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagehashes
        fields = ['image_hash']
