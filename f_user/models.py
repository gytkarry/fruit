from django.db import models

# Create your models here.
class User(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    uemil=models.EmailField(max_length=30)
    urelname=models.CharField(max_length=20,default='')
    uadr=models.CharField(max_length=100,default='')
    uphone=models.CharField(max_length=11,default='')
    usex=models.CharField(max_length=2,default='0')

class Address(models.Model):
    uid=models.IntegerField()
    reciver=models.CharField(max_length=20,help_text='收件人')
    sheng=models.CharField(max_length=8,default='')
    shi=models.CharField(max_length=16,default='')
    qu=models.CharField(max_length=16,default='')
    detialaddr=models.CharField(max_length=100,default='')
    yzbm=models.CharField(max_length=6,default='150001')
    rphone=models.CharField(max_length=11,default='')
    mrdz=models.BooleanField(max_length=1,default='0')
    scbz=models.BooleanField(max_length=1,default=0)
