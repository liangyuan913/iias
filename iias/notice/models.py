from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-pubDateTime']
    
class Comment(models.Model):
    notice = models.ForeignKey(Notice, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    pubDateTime = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.notice.title + '-' + str(self.id)
    
    class Meta:
        ordering = ['pubDateTime']
