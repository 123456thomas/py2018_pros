from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Users)
class Usermodel(admin.ModelAdmin):
    list_display = ['username','age','catime','pwd']
    list_filter = ['username']
    list_per_page = 3
    list_display_links = ['age','username']
    fields = ['username','age','pwd']
    actions_on_bottom = True
    actions_on_top = False


admin.site.register(models.Articles)

# 后台中用户管理方案一
# admin.site.register(models.Users,Usermodel)
# 后台中用户管理方案二,添加
# @admin.register(models.Users)