from django.db import models
import os

# def upload_file(instance, filename):
#     # Define the upload path for the file
#     upload_path = 'logo/'
    
#     # Generate a unique filename for the uploaded file
#     unique_filename = f"{instance.pk}_{filename}"
    
#     # Construct the full file path
#     file_path = os.path.join(upload_path, unique_filename)
    
#     # # Create the directory if it doesn't exist
#     # os.makedirs(upload_path, exist_ok=True)
    
#     # Save the uploaded file to the specified path
#     with open(file_path, 'wb+') as destination:
#         for chunk in instance.thumbnail.chunks():
#             destination.write(chunk)
    
#     # Return the file path or unique filename if needed
#     return file_path or unique_filename

def delete_file(file_path):
    # Delete the file from the filesystem
    if os.path.exists(file_path):
        os.remove(file_path)

# Create your models here.
class JobType (models.Model):
    type = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.type

class Job (models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    position = models.CharField(max_length=255, blank=False)
    job_type = models.ManyToManyField(JobType, related_name='jobtype')
    address = models.CharField(max_length=255, blank=False)
    longitude = models.FloatField(blank=False)
    latitude = models.FloatField(blank=False)
    thumbnail = models.ImageField(upload_to='logo/', blank=False)
    contact_num = models.IntegerField(blank=False)
    available = models.BooleanField()
    email_add = models.EmailField()

    def __str__(self):
        return self.name

    
