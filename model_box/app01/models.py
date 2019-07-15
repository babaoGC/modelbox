from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserInfo(AbstractUser):
    phone = models.BigIntegerField(null=True, blank=True)
    face = models.FileField(upload_to='face/', default='face/default.png')
    user_type = models.IntegerField(choices=((1, '管理员'), (0, '普通用户')), default=0)
    points = models.IntegerField(default=0,null=True)  # 会员积分
    is_locked = models.IntegerField(default=0, null=True)
    purse = models.IntegerField(null=True, default=0)

    collect = models.ManyToManyField(to='Collect')  # 用户收藏模型表
    follow = models.ManyToManyField(to='Follow')   # 用户关注表
    download = models.ManyToManyField(to='Download')


    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = '用户表'

class Follow(models.Model):
    f_user=models.IntegerField()
    f_time=models.DateField(auto_now_add=True)



class Collect(models.Model):
    model=models.IntegerField()
    collect_time=models.DateField(auto_now_add=True)



class Pay(models.Model):
    user = models.ForeignKey(to='UserInfo')
    money = models.DecimalField(max_digits=5, decimal_places=2)
    create_time = models.DateField(auto_now_add=True)


class Expend(models.Model):
    user = models.ForeignKey(to='UserInfo')
    money = models.DecimalField(max_digits=5, decimal_places=2)
    create_time = models.DateField(auto_now_add=True)


class Model(models.Model):
    name = models.CharField(max_length=32)
    user = models.ForeignKey(to='UserInfo')

    path = models.CharField(max_length=255)
    md5 = models.CharField(max_length=255)
    price = models.IntegerField()
    file_size = models.CharField(max_length=32)
    position = models.CharField(max_length=9, null=True) # 模型排序位置权重

    collect_num = models.IntegerField(null=True, default=0) #收藏次数
    download_num = models.IntegerField(null=True, default=0) # 下载此时

    choice = (
        (0, 'SketchUp 8.0'), (1, 'SketchUp 2013'), (2, 'SketchUp 2014'), (3, 'SketchUp 2015'), (4, 'SketchUp 2016'),
        (5, 'SketchUp 2017'), (6, 'SketchUp 2018'), (7, 'SketchUp 2019'))
    version = models.IntegerField(choices=choice, default=0) #模型版本

    choice = ((0, '现代'), (1, '中式'), (2, '美式'), (3, '北欧'))
    style = models.IntegerField(choices=choice, default=0)  #  模型风格

    introduce = models.TextField(max_length=255, null=True) # 模型简介


    tag = models.ManyToManyField(to='Tag')
    category=models.ForeignKey(to='Category')

class Picture(models.Model):
    model = models.ForeignKey(to='Model')
    path = models.FileField(upload_to='picture/')


class Tag(models.Model):
    name = models.CharField(max_length=32)


class Category(models.Model):
    name = models.CharField(max_length=32)
    parent=models.IntegerField(null=True)


class Comment(models.Model):
    user=models.ForeignKey('UserInfo')
    model=models.ForeignKey(to='Model')
    content=models.TextField(max_length=255)
    create_time=models.DateField(auto_now_add=True)
    parent = models.IntegerField(null=True)


class Download(models.Model):
    model = models.ForeignKey(to='Model')
    download_time=models.DateField(auto_now_add=True)