from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView)
from .serializers import (ImageHashSerializer,
                          ImageWordesSerializer,
                          ImageInputSerializer,
                          HashSerializer)
from .models import Imagehashes
from rest_framework.response import Response
from rest_framework import status



class ImageHashView(ListAPIView):
    queryset = Imagehashes.objects.all()
    serializer_class = ImageHashSerializer


class ImageWordsView(RetrieveAPIView):
    queryset = Imagehashes.objects.all()
    serializer_class = ImageWordesSerializer
    lookup_field = 'image_hash'


class InputView(CreateAPIView):
    queryset = Imagehashes.objects.all()
    serializer_class = ImageInputSerializer
    lookup_field = 'image_hash'

    # def post(self, request):
    #     serializer = ImageInputSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HashView(ListAPIView):
    queryset = Imagehashes.objects.all()
    serializer_class = HashSerializer
