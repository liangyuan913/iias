from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.article.title + '-' + str(self.id)
