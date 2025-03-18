from django.db import models

# Create your models here.
class Product(models.Model):
    LIVE=1
    DELETE=0
    DELETE_CHOICES=((LIVE,'live'),(DELETE,'Delete')) #for adding to recyclebin before deleting permanently

    title=models.CharField(max_length=200)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/')
    priority=models.IntegerField(default=0)
    delete_status=models.IntegerField(default=LIVE)
    created_at=models.DateTimeField(auto_now_add=True) #for the recording of date and time when the data is updated and created
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
