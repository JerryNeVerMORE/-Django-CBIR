from django.db import models

# Create your models here.


class Img(models.Model):
    img_url = models.ImageField(upload_to='img') # upload_to指定图片上传的途径，如果不存在则自动创建
    img_name = models.TextField(default="pics")
    img_tags = models.TextField(default="tags")
    img_uploader = models.TextField(default="0")


class Article(models.Model):
    title = models.CharField(u'标题', max_length=256,default="title")
    content = models.TextField(u'内容',default="content")
    pub_date = models.DateTimeField(u'发表时间', auto_now=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.title


class Usr(models.Model):
    user_name = models.CharField(max_length=10,unique=True)
    user_pass = models.CharField(max_length=10)

