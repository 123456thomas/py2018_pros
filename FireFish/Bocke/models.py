from django.db import models
import datetime

# Create your models here.

class Artmanage(models.Manager):
    # 写文章方法
    def Writeart(self, title, content, author_id):
        wart = self.create(artname=title,arttext=content,ctime=datetime.datetime.now(),author=author_id)
        wart.save()
        return True

        pass
    def Findart(self):
        pass
    def Getart(self):
        pass
    def Delart(self):
        pass
# 方法三：创建类的管理器
class Usermanage(models.Manager):
    # 增加
    def create_user(self, name, pwd,age=None,id=None):
        user = self.create(username=name, pwd=pwd,age=age,id=id)
        return user

    # 查看所有
    def findall(self):
        infoall = self.all()
        return infoall

    # 查找一个
    def getone(self, id):
        infone = self.get(id=id)
        return infone

    # 修改一个
    def update(self, id, name):
        user=self.filter(id=id)
        user.username=name
        return user

    # 删除一个
    def delone(self, id):
        user=self.filter(id=id)
        user.delete()


# 创建用户
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=12,unique=True)
    pwd = models.CharField(max_length=40,default="123456")
    age = models.IntegerField(default=18)
    usermanage = Usermanage()

    @classmethod
    def Create(cls, name, pwd="123456", id=0):
        author = cls(username=name, pwd=pwd, id=id)
        return author
    def __str__(self):
        # 在打印对象时进行覆盖
        return self.username


# 创建文章类
class Artiles(models.Model):
    id = models.AutoField(primary_key=True)
    artname = models.CharField(max_length=60)
    arttext = models.TextField()
    ctime = models.DateTimeField(default=datetime.datetime.now())
    author = models.ForeignKey(Users, on_delete=models.CASCADE)
    artmanage =Artmanage()


