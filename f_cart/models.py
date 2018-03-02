from django.db import models
from f_user.models import User
from f_goods.models import GoodInfo

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey('f_user.User',None)
    goods=models.ForeignKey('f_goods.GoodInfo',None)
    count=models.IntegerField(default=0)