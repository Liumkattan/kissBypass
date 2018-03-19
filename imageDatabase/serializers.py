from rest_framework import serializers
from .models import Imagehashes


class ImageHashSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagehashes
        fields = ('image_hash', 'image_words')


class ImageWordesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagehashes
        fields = ('image_words')
