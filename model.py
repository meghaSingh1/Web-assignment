from django.db import models

class MovieInfo(models.Model):
	movie_name = models.CharField(max_length=200)
	phone_number= models.IntegerField()
	email= models.CharField(max_length=500)
	pic = models.IntegerField(upload_to = 'pic_folder/',default='pic_folder/None/no.img.jpg')
    video= models.FileField(upload_to='documents/')
	option=models.CharField(max_length=100)