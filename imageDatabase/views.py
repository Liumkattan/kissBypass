from rest_framework.generics import ListAPIView
from .serializers import ImageHashSerializer, ImageWordesSerializer
from .models import Imagehashes


class ImageHashView(ListAPIView):
    queryset = Imagehashes.objects.all()
    serializer_class = ImageHashSerializer


class ImageWordsView(ListAPIView):
    queryset = Imagehashes.objects.all()
    serializer_class = ImageWordesSerializer
    lookup_field = 'image_hash'
