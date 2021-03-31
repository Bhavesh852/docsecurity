from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doc_Detail(models.Model):
	doc_id = models.AutoField(primary_key=True)
	doc_user = models.ForeignKey(User, on_delete=models.CASCADE) 
	doc_category = models.CharField(max_length=20)
	doc_title = models.CharField(max_length=30)
	doc_tech = models.CharField(max_length=30)
	doc = models.FileField(upload_to='userportal/document')

	def __str__(self):
		return self.doc_title 


class Private_Doc(models.Model):
	p_id = models.AutoField(primary_key=True)
	pdoc_user = models.ForeignKey(User, on_delete=models.CASCADE) 
	pdoc_category = models.CharField(max_length=20)
	pdoc_title = models.CharField(max_length=30)
	pdoc_tech = models.CharField(max_length=30)
	pdoc_pass = models.CharField(max_length=20)
	pdoc = models.FileField(upload_to='userportal/document')

	def __str__(self):
		return self.pdoc_title 

class Contact(models.Model):
	c_id = models.AutoField(primary_key=True)
	c_first_name = models.CharField(max_length=30)
	c_last_name = models.CharField(max_length=30)
	c_email = models.EmailField(max_length=200)
	c_msg = models.CharField(max_length=255)

	def __str__(self):
		return self.c_first_name


