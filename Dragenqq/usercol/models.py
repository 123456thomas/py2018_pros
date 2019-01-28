from django.db import models
# 导入副文本编辑器
import datetime
from tinymce.models import HTMLField

content = HTMLField
# Create your mode
# ls here.




# 类管理器
class Usersmanage(models.Manager):
    def Create_user(self, name, pwd, email, age=18):
        user = self.create(username=name, pwd=pwd, email=email, age=age)
        user.save()




# 创建用户类
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, verbose_name='作者')
    pwd = models.CharField(max_length=50)
    email = models.EmailField()
    catime = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)
    age = models.PositiveIntegerField(default=18)
    photo = models.ImageField(upload_to='static/upload/head', null=True)
    usermanage = Usersmanage()

    def __str__(self):
        return self.username


# 好友类
class Friends(models.Model):
    id = models.AutoField(primary_key=True)
    partner = models.CharField(verbose_name='好友',max_length=255 ,null=True,blank=True)
    offer = models.CharField(verbose_name='好友申请',max_length=255 ,null=True,blank=True)
    oid = models.ForeignKey(Users, on_delete=models.CASCADE)


# 创建文章类
class Articles(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,verbose_name='标题')
    # content = models.TextField()
    content = HTMLField(verbose_name='内容')
    ctime = models.DateTimeField(verbose_name='创作时间',auto_now_add=True)
    utime = models.DateTimeField(verbose_name='修改时间', auto_now=True)
    img = models.ImageField(upload_to='static/upload/imgs', null=True, blank=True)
    fid = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='作者')
