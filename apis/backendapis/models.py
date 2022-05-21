from django.db import models



# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'media/{filename}'.format(filename=filename)

class FileDownloaderModel(models.Model):

    fileType = models.CharField(max_length=255, blank=True, null=True)
    sheetName = models.CharField(max_length=255, blank=True, null=True)
    uploadedFile = models.FileField(upload_to=upload_to, blank=True, null=True)
    isFilePicked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.uploadedFile.delete()
        return super().delete(*args, **kwargs)
