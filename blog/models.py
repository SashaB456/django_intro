from django.db import models

# Create your models here.
class Authors(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
class Posts(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE, null=True)
#    def published_recently(self, published_date):
#        current_date = models.DateTimeField(auto_now=True)
#        if current_date - published_date < "7 days":
#            return True
#       else:
#            return False
    def __str__(self):
        return f"{self.title}, {self.content}"