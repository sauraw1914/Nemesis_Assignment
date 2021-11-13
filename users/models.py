from django.db import models

class userModel(models.Model):
    username=models.CharField(max_length=15)
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=30)
    address=models.CharField(max_length=30)

    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=email,
            username=username,
            password=password,
        )
# Create your models here.
