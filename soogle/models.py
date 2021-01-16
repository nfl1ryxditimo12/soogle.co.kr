from django.db import models

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=64, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    create_date = models.DateTimeField(verbose_name='등록시간')

    def __str__(self):
        return self.title

    class Meta:
        db_table = '글'
        verbose_name = '글'
        verbose_name_plural = '글'
