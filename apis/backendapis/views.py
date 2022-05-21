from requests import delete
from .models import FileDownloaderModel
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import FileDownloaderSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from .business import DownloadContent



class FileUploadViewset(viewsets.ModelViewSet):
    queryset = FileDownloaderModel.objects.all()
    serializer_class = FileDownloaderSerializer
    parser_classes = (MultiPartParser, FormParser)

    def create(self, request, *args, **kwargs):
        print("request.data" , request.data, self.request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()


class DownloadView(APIView):

    def get(self, request, format=None):
        print("btn clicked !!!")
        return Response(status=status.HTTP_200_OK)

    def post(self, request, format=None):
        btnId = self.request.data
        btnId = btnId['btnId']
        queryset = FileDownloaderModel.objects.get(id=btnId)
        print(queryset.uploadedFile)
        file_path = queryset.uploadedFile
        sheet_name = queryset.sheetName
        file_type = queryset.fileType
        obj = DownloadContent(file_path=file_path, sheet_name=sheet_name, file_type=file_type)
        return Response(status=status.HTTP_201_CREATED)

    # def delete(self, request, format=None):
    #     queryset = FileDownloaderModel.objects.get(id=id)


class DeleteView(APIView):
    def post(self, request, format=None):
        btnId = self.request.data
        btnId = btnId['btnId']
        queryset = FileDownloaderModel.objects.get(id=btnId)
        queryset.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



