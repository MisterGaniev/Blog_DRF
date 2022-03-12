from django.db import models

# Create your models here.

class Maqola(models.Model):
    title = models.CharField(max_length=100)
    matn = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.title}'

class Images(models.Model):
    image = models.FileField(upload_to='maqola_images')
    connection = models.ForeignKey(Maqola, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.connection.title}'