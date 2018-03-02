from django.contrib import admin
from f_goods.models import GoodInfo,TypeInfo,GoodsImage
# Register your models here.
admin.site.register(TypeInfo)
admin.site.register(GoodInfo)
admin.site.register(GoodsImage)
