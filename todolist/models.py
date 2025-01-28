from django.db import models
class todolist(models.Model):
    Title=models.CharField(max_length=10)
    Description = models.CharField(max_length=255, default="No description")
    status=models.BooleanField(default=False)
    time_of_completion=models.DateTimeField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
def __str__(self):
    return self.Title

