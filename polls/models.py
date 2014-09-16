from django.db import models

# Create your models here.
class Question(models.Model):
	qustion_text = models.CharField(max_length=200)
	pub_date = models.DataTimeField('date published')
	
class Choice(models.Model):
	question = models.ForeignKey(Question)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)