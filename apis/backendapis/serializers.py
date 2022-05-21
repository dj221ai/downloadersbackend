from rest_framework import serializers
from .models import FileDownloaderModel


class FileDownloaderSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(FileDownloaderSerializer, self).__init__(many=many, *args, **kwargs)

    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = FileDownloaderModel
        fields = '__all__'
