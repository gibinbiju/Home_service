from django.db import models

# Create your models here.

class State(models.Model):
    S_name=models.CharField(max_length=100)
    def __str__(self):
        return self.S_name

class District(models.Model):
    d_name=models.CharField(max_length=100)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    def __str__(self):
        return self.d_name

class Area(models.Model):
    a_name=models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    def __str__(self):
        return self.a_name

class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=120)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=100)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    district=models.ForeignKey(District,on_delete=models.CASCADE)
    area=models.ForeignKey(Area,on_delete=models.CASCADE)
    def __str__(self):
        return self.username


